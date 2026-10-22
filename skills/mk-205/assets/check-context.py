#!/usr/bin/env python3
"""Check a source-bound Skill contract against brand and task snapshots."""
import argparse, hashlib, json, re, math
from urllib.parse import urlparse
from decimal import Decimal
from pathlib import Path
from datetime import datetime, timezone

def json_stringify(value):
    if value is None or isinstance(value,(str,bool)):return json.dumps(value,ensure_ascii=False,separators=(',',':'))
    if isinstance(value,(int,float)):
        if not math.isfinite(value):raise ValueError('CONTEXT_NUMBER_NOT_FINITE')
        if value==0:return '0'
        if 1e-6<=abs(value)<1e21:
            return str(int(value))if int(value)==value else format(Decimal(repr(value)),'f')
        mantissa,exponent=format(float(value),'.16e').split('e')if isinstance(value,int)else repr(value).lower().split('e')
        mantissa=mantissa.rstrip('0').rstrip('.')if '.'in mantissa else mantissa
        return mantissa+'e'+('+'if int(exponent)>=0 else '-')+str(abs(int(exponent)))
    if isinstance(value,list):return '['+','.join(json_stringify(v)for v in value)+']'
    return '{'+','.join(json.dumps(k,ensure_ascii=False)+':'+json_stringify(v)for k,v in value.items())+'}'

def digest(value):
    raw=value if isinstance(value,str) else json_stringify(value)
    return hashlib.sha256(raw.encode()).hexdigest()

def reviewed_evidence_digest(e):
    def stable(v):
        if isinstance(v,list):return [stable(x)for x in v]
        if isinstance(v,dict):return {k:stable(v[k])for k in sorted(v)}
        return v
    return digest(stable(e))

def check(contract, request, context, task=None, now=None):
    now=now or datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    stage=contract['stages'][request['stage']]
    scope={**(task or {}).get('scope',{}),**request.get('scope',{})}
    if request.get('brand_key'):scope['brand_key']=request['brand_key']
    if task and (task['skill_id']!=contract['skill_id'] or task['stage']!=request['stage'] or any(scope.get(k)!=v for k,v in task['scope'].items())):raise ValueError('TASK_SCOPE_MISMATCH')
    sources={e['id']:e for e in context.get('evidence',[])+(task or {}).get('evidence',[])}
    for e in sources.values():
        m=e.get('social')
        if m:
            kinds={'profile':'profile','post':'text','video_description':'metadata_only','transcript':'transcript','audiovisual_analysis':'audiovisual','comment':'text'}
            if m.get('content_kind')not in kinds or m.get('coverage')!=kinds[m['content_kind']]:raise ValueError('CONTEXT_EVIDENCE_SCHEMA_INVALID')
            if m.get('platform')not in ['facebook','instagram','threads','x','linkedin','youtube']or not all(isinstance(m.get(k),str)and m[k].strip()for k in ['source_id','collection_id','platform_content_id'])or type(m.get('source_revision'))is not int or m['source_revision']<1:raise ValueError('CONTEXT_EVIDENCE_SCHEMA_INVALID')
            if m['content_kind']in ['transcript','audiovisual_analysis']:
                start,end=m.get('start_seconds'),m.get('end_seconds')
                if any(type(v)not in [int,float]or not math.isfinite(v)for v in [start,end])or start<0 or end<=start:raise ValueError('CONTEXT_EVIDENCE_SCHEMA_INVALID')
            if m['content_kind']=='transcript'and(not isinstance(m.get('language'),str)or not m['language'].strip()or m.get('transcript_origin')not in ['manual','automatic','translated']):raise ValueError('CONTEXT_EVIDENCE_SCHEMA_INVALID')
            if m['content_kind']=='audiovisual_analysis':
                a=m.get('analysis',{})
                if not all(isinstance(a.get(k),str)and a[k].strip()for k in ['reader','receipt'])or not isinstance(a.get('modes'),list)or not 1<=len(a['modes'])<=2 or any(v not in ['audio','visual']for v in a['modes']):raise ValueError('CONTEXT_EVIDENCE_SCHEMA_INVALID')
        if digest(e['excerpt'])!=e['content_sha256']:raise ValueError('CONTEXT_EVIDENCE_HASH_MISMATCH')
        if e['source_type']=='website'and re.fullmatch(r'(?:(?:www|m)\.)?(?:facebook\.com|fb\.com|instagram\.com|threads\.(?:com|net)|x\.com|twitter\.com|linkedin\.com|youtube\.com)',urlparse(e['source']).hostname or '')and not e.get('social'):raise ValueError('CONTEXT_SOCIAL_METADATA_REQUIRED')
        if e['source'].split(':')[0].lower() in ['model','assistant','generated','hypothesis']:raise ValueError('CONTEXT_SOURCE_NOT_ORIGINAL')
    for d in context.get('data',[])+(task or {}).get('data',[]):
        linked=[sources.get(e) for e in d['evidence_ids']]
        if not linked or any(e is None for e in linked):raise ValueError('CONTEXT_EVIDENCE_MISSING')
        if any(any(d['scope'].get(k)!=v for k,v in e['scope'].items())for e in linked):raise ValueError('CONTEXT_EVIDENCE_SCOPE_MISMATCH')
        if d['state']=='data_supported' and not any(e['source_type']=='report'for e in linked):raise ValueError('CONTEXT_REPORT_EVIDENCE_REQUIRED')
        conf=d.get('confirmation',{})
        if d['state']=='user_confirmed' and not any(e['source_type'] in ['conversation','approved_document'] and e['source']==conf.get('source') and conf.get('excerpt') and conf['excerpt'] in e['excerpt'] for e in linked):raise ValueError('CONTEXT_CONFIRMATION_EVIDENCE_REQUIRED')
    for item in [context]+([task]if task else []):
        for d in item.get('data',[]):
            ds=d['scope'];v=d['value']
            if ds.get('period_start')and ds.get('period_end')and ds['period_start']>ds['period_end']:raise ValueError('CONTEXT_PERIOD_INVALID')
            if v['type']=='number'and(not math.isfinite(v['number'])or(re.fullmatch('[A-Z]{3}',v['unit'])and v['unit']!=ds.get('currency'))):raise ValueError('CONTEXT_NUMBER_INVALID')
            if d['field']in ['offer.price','rule.target_cpa','task.spend','task.net_revenue','task.non_ad_cost','task.unaccounted_fixed_cost','task.variable_cost','task.fixed_cost']and(v['type']!='number'or not ds.get('currency')or v['unit']!=ds['currency']):raise ValueError('CONTEXT_AMOUNT_INVALID')
    used={}
    def valid_confirmation(e,key):
        return isinstance(e,dict)and e.get('source_type')in ['conversation','approved_document']and not e.get('social')and not re.match(r'^(model|assistant|generated|hypothesis):',e.get('source',''),re.I)and bool(key)and e.get('scope',{}).get('brand_key')==key and bool(e.get('excerpt'))and digest(e['excerpt'])==e.get('content_sha256')
    def social_usable(e):
        m=e.get('social')
        if not m:return True
        a=next((a for a in context.get('source_accounts',[])if a['id']==m['source_id']),None)
        r=next((r for r in context.get('source_reviews',[])if r['id']==m.get('review_id')and r['status']=='approved'),None)
        if not a or a['status']!='confirmed' or a['revision']!=m['source_revision']or not valid_confirmation(a.get('confirmation'),e['scope'].get('brand_key'))or not r or not valid_confirmation(r.get('confirmation'),e['scope'].get('brand_key'))or r['source_revisions'].get(a['id'])!=a['revision']:return False
        return a.get('confirmed_identity_sha256')==digest(dict(platform=a['platform'],identity=a.get('platform_id')or a['url']))and r.get('evidence_sha256',{}).get(e['id'])==reviewed_evidence_digest(e)
    def active(d):
        return d.get('status','active')=='active' and all((not x.get('valid_from') or x['valid_from']<=now)and(not x.get('valid_until')or x['valid_until']>=now)for x in [d]+[sources[i]for i in d['evidence_ids']]) and all(social_usable(sources[i])for i in d['evidence_ids'])
    def evaluate(n):
        if n.get('condition'):
            decision=(task or {}).get('decisions',{}).get(n['condition']['id'])
            if not decision:return [dict(field=n['condition']['id'],reason='branch_decision',location='task')]
            if not decision['applies']:return []
        if 'field' in n:
            if n.get('task_property')=='original_question' and (task or {}).get('original_question','').strip():return []
            pool=context.get('data',[]) if n['location']=='context' else (task or {}).get('data',[]) if n['location']=='task' else context.get('data',[])+(task or {}).get('data',[])
            candidates=[d for d in pool if d['field']==n['field'] and(not n.get('kind')or d['kind']==n['kind'])]
            keys=set(n['scope'])|(set(scope)if n['location']=='task'else set())
            scoped=[d for d in candidates if all(k in scope and d['scope'].get(k)==scope[k]for k in keys)and all(k not in d['scope']or d['scope'][k]==v for k,v in scope.items())]
            valid=[d for d in scoped if active(d)and d['state']in n['states']and d['value']['type']in n['value_types']and(n.get('quantity')!='amount'or(d['value']['type']=='number'and d['value']['unit']==d['scope'].get('currency')))and(n.get('quantity')!='ratio'or(d['value']['type']=='number'and not re.fullmatch('[A-Z]{3}',d['value']['unit'])))and(n.get('quantity')!='count'or(d['value']['type']=='number'and d['value']['number']>=0 and int(d['value']['number'])==d['value']['number']and not re.fullmatch('[A-Z]{3}',d['value']['unit'])))and(not n.get('evidence_roles')or any(sources[i].get('source_role')in n['evidence_roles']for i in d['evidence_ids']))]
            coverage=next((r['minimum_coverage']for r in contract.get('social_evidence',{}).get('field_requirements',[])if r['field']==n['field']),None)
            if coverage:valid=[d for d in valid if not any(sources[i].get('social')for i in d['evidence_ids'])or any((sources[i].get('social',{}).get('coverage')in ['transcript','audiovisual']if coverage=='video_body'else sources[i].get('social',{}).get('coverage')==coverage) for i in d['evidence_ids'])]
            def proofs(d):
                return [p for p in context.get('data',[])+(task or {}).get('data',[])if p['field']=='claim.proof'and p['state']in ['source_stated','user_confirmed','data_supported']and all(k in d['scope']and p['scope'].get(k)==d['scope'][k]for k in ['brand_key','product_id','product_version'])and all(k not in p['scope']or p['scope'][k]==v for k,v in d['scope'].items())and active(p)and any(r['relation']=='proof'and r['target_id']==p['id']for r in d.get('relations',[]))]
            if n.get('requires_proof'):valid=[d for d in valid if proofs(d)]
            usable=list({d['entity_id']:d for d in valid}.values())
            def fail(reason):return [dict(field=n['field'],reason=reason,location=n['location'])]
            if len(usable)<n['min_count']or('exact_count'in n and len(usable)!=n['exact_count']):
                reason='conflicting'if any(d.get('status')=='conflicting'for d in scoped)else'stale_or_unread_evidence'if any(not active(d)for d in scoped)else'unconfirmed'if any(d['state']not in n['states']for d in scoped)else'scope_mismatch'if candidates and not scoped else'missing'
                social=any(sources[i].get('social')for d in scoped for i in d['evidence_ids'])
                if social and any(not active(d)for d in scoped):reason='unconfirmed_social_source'
                elif social and coverage:reason='social_coverage_missing'
                return fail(reason)
            if any(d.get('status')=='conflicting'for d in scoped)or(n['field']in ['brand.identity','rule.target_cpa','rule.target_roas','rule.ranking','rule.adjustment','offer.price']and len({digest(d['value'])for d in valid})>1):return fail('conflicting')
            used.update({d['id']:d for d in usable})
            if n.get('requires_proof'):used.update({p['id']:p for d in usable for p in proofs(d)})
            return []
        if 'any'in n:
            results=[]
            for child in n['any']:
                before=used.copy();result=evaluate(child);selected=used.copy();used.clear();used.update(before)
                if not result:used.update(selected);return []
                results+=result
            return [{**r,'reason':'any_of:'+r['reason']}for r in results]
        return [r for child in n.get('all',[])for r in evaluate(child)]
    missing=evaluate(stage['requires'])
    if contract['skill_id']=='MK-135'and request['stage']=='copy'and not missing:
        proofs={d['id']for d in used.values()if d['field']=='claim.proof'}
        for d in list(used.values()):
            if d['field']=='claim.usp'and not any(x['relation']=='proof'and x['target_id']in proofs for x in d.get('relations',[])):missing.append(dict(field=d['id'],reason='missing_proof_link',location='context'))
    if task and 'expected_task_revision'in request and task['revision']!=request['expected_task_revision']:missing.append(dict(field='task.revision',reason='revision_conflict',location='task'))
    data={d['id']:d for d in context.get('data',[])}
    for old in (task or {}).get('used_context',[]):
        if old['id']not in data or digest(data[old['id']])!=old['sha256']:missing.append(dict(field=old['id'],reason='changed_dependency',location='context'))
    if 'expected_context_revision'in request and request['expected_context_revision']!=context['revision']and not(task or {}).get('used_context'):missing.append(dict(field='context.revision',reason='revision_conflict',location='context'))
    reasons=' '.join(r['reason']for r in missing)
    needs_context=any(r['location']!='task'for r in missing)
    status='conflicting_context'if any(r in reasons for r in ['conflicting','revision_conflict','changed_dependency'])else'needs_decision'if any(r in reasons for r in ['unconfirmed','branch_decision'])else'needs_create'if needs_context and not context['revision']else'needs_context'if needs_context else'needs_task_data'if missing else'ready'
    available=[]
    if status not in ['ready','conflicting_context']:
        for name,candidate in contract['stages'].items():
            if name==request['stage'] or not candidate['delivery']:continue
            before=used.copy();problems=evaluate(candidate['requires']);used.clear();used.update(before)
            if not problems:available.append(dict(stage=name,allowed_output=candidate['allowed_output']))
    return dict(skill_id=contract['skill_id'],stage=request['stage'],status=status,available_stages=available,execution_allowed=status=='ready',delivery_allowed=status=='ready'and stage['delivery'],missing=missing,used_context=[dict(id=d['id'],sha256=digest(d))for d in used.values()if d['id']in data])

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--contract',type=Path,required=True);p.add_argument('--snapshot',type=Path,required=True);p.add_argument('--method',type=Path,required=True);p.add_argument('--purpose',choices=['start','delivery'],default='delivery');a=p.parse_args()
    c=json.loads(a.contract.read_text());snapshot=json.loads(a.snapshot.read_text())
    if hashlib.sha256(a.method.read_bytes()).hexdigest()!=c.get('method_sha256',c['source_sha256']):raise ValueError('CONTEXT_SKILL_VERSION_MISMATCH')
    result=check(c,snapshot['input'],snapshot['context'],snapshot.get('task'),snapshot.get('now'))
    print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['delivery_allowed'if a.purpose=='delivery'else'execution_allowed']else 1)
