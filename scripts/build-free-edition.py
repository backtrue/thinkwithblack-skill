#!/usr/bin/env python3
"""Build the public upload packs and identical download artifact using stdlib."""
from pathlib import Path
from urllib.parse import unquote
import argparse, hashlib, json, re, zipfile, runpy

ROOT=Path(__file__).resolve().parents[1]
DOCS=['README.md','START_HERE.md','PUBLIC_SKILL_RULES.md','PUBLIC_BOUNDARY.md','LICENSE',
      'RELEASE.md','CHANGELOG.md','CONTRIBUTING.md','context/MARKETING_CONTEXT.template.md',
      'examples/README.md','examples/product-facts.md','examples/cookie-costs.md','examples/cookie-repeat.md','examples/event-forecast.md','examples/member-rules.md']
MAINTENANCE=['scripts/build-free-edition.py','scripts/verify-public-skills.py','tests/test_free_edition.py',
             '.github/workflows/prepare-thinkwithblack-release.yml','.gitignore',
             'scripts/build-english-edition.py','tests/test_english_edition.py']
FORBIDDEN=['.codex-plugin','.agents','.app.json','openai.yaml','validate-skill-run.py','check_assets.py']
PRODUCT_PATTERNS=[r'THINKWITHBLACK_SYNC',r'Entry Router',r'approval_token',r'unsupported_by_current_mcp',
                  r'(?i)MCP runtime',r'TWB_REPOSITORY_READ_TOKEN',r'backtrue/thinkwithblack-mcp',
                  r'"sourceCommit"',r'"sourceRepository"',r'record\.json',r'first read',r'check_assets\.py']
LINK=re.compile(r'\[[^\]\n]+\]\(([^)\n]+)\)')

def sha(data):return hashlib.sha256(data).hexdigest()
def safe(root,rel):
    p=(root/rel).resolve()
    if not p.is_relative_to(root.resolve()):raise ValueError('Path outside repository: '+rel)
    if (root/rel).is_symlink():raise ValueError('Symlink is not a public source: '+rel)
    return p

def load(root):
    m=json.loads((root/'free-content.json').read_text())
    if not re.fullmatch(r'[0-9A-Za-z.-]+',m['version']):raise ValueError('Invalid version')
    ids=set();sources=set();packs=set()
    for e in m['entries']:
        if e['id'] in ids or e['source'] in sources or e['pack'] in packs:raise ValueError('Duplicate public entry')
        ids.add(e['id']);sources.add(e['source']);packs.add(e['pack'])
        if not re.fullmatch(r'packs/[a-z0-9-]+\.md',e['pack']):raise ValueError('Invalid pack path')
        for f in [e['source']]+e['references']:
            if not safe(root,f).is_file():raise ValueError('Missing source: '+f)
            if any(x in Path(f).parts for x in FORBIDDEN):raise ValueError('Product file: '+f)
    actual={str(p.relative_to(root)) for group in ['skills','extensions'] for p in (root/group).glob('*/SKILL.md')}
    if actual!=sources:raise ValueError('Public method inventory mismatch: '+str(sorted(actual^sources)))
    for e in m.get('supplements',[]):
        identifier=e['id'];prefix='supplements/'+identifier+'/'
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',identifier) or identifier in ids:raise ValueError('Invalid supplemental ID')
        if e['source']!=prefix+'SKILL.md' or e['pack']!='packs/'+identifier+'.md' or e.get('language')!='zh-TW':raise ValueError('Invalid supplemental mapping')
        ids.add(identifier)
        for rel in [e['source']]+e['references']:
            if not rel.startswith(prefix) or not safe(root,rel).is_relative_to((root/prefix).resolve()):raise ValueError('Supplemental path outside Skill')
            if not safe(root,rel).is_file():raise ValueError('Missing supplemental source: '+rel)
            if any(x in Path(rel).parts for x in FORBIDDEN):raise ValueError('Product file: '+rel)
    return m

def source_files(m):
    return sorted(set(DOCS+['free-content.json']+[f for e in m['entries']+m.get('supplements',[]) for f in [e['source']]+e['references']]))

def render_supplement(root,entry,version):
    refs=entry['references']
    anchors={safe(root,rel):'supplement-reference-'+str(i) for i,rel in enumerate(refs,1)}
    chunks=[f'# {entry["name"]}\n\n版本：{version}｜原文語言：{entry["language"]}']
    for rel in [entry['source']]+refs:
        text=safe(root,rel).read_text()
        if rel==entry['source']:text=re.sub(r'\A---\n.*?\n---\n','',text,flags=re.S)
        def replace(match):
            target=local_link(root,rel,match[1])
            if target in anchors:return match[0].replace('('+match[1]+')','(#'+anchors[target]+')')
            return match[0]
        text=LINK.sub(replace,text).strip()
        if rel in refs:chunks.append(f'<a id="{anchors[safe(root,rel)]}"></a>\n\n## 附錄：{Path(rel).name}\n\n'+text)
        else:chunks.append(text)
    return ('\n\n'.join(chunks)+'\n').encode()

def local_link(root,current,link):
    link=unquote(link.strip('<>')).split('#',1)[0]
    if not link or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',link):return None
    return safe(root,str(Path(current).parent/link))

def render_pack(root,e,version):
    refs=e['references'];files=[e['source']]+refs
    anchors={(root/p).resolve(): 'reference-'+str(i) for i,p in enumerate(refs,1)}
    def render(rel):
        t=(root/rel).read_text()
        if rel==e['source']:
            t=re.sub(r'\A---\n.*?\n---\n','',t,flags=re.S)
            t=re.sub(r'^一般對話請上傳.*\n','',t,flags=re.M)
        def replace(match):
            target=local_link(root,rel,match[1])
            if target in anchors:return match[0].replace('('+match[1]+')','(#'+anchors[target]+')')
            if target==(root/'PUBLIC_SKILL_RULES.md').resolve():return '[共用規則](#common-rules)'
            return match[0]
        t=LINK.sub(replace,t)
        # Some inherited asset references are plain text rather than Markdown links
        for dep in refs:
            relative=str(Path(dep).relative_to(Path(e['source']).parent))
            if relative in t:
                t=t.replace(relative,'[附錄：'+Path(dep).name+'](#'+anchors[(root/dep).resolve()]+')')
        return t.strip()
    chunks=[f'# {e["id"]}｜{e["name"]} 方法包\n\n教材版本：{version}',
            '<a id="common-rules"></a>\n\n'+(root/'PUBLIC_SKILL_RULES.md').read_text().strip(),
            render(e['source'])]
    for rel in refs:
        anchor=anchors[(root/rel).resolve()]
        body=(root/rel).read_text().strip()
        if rel.endswith('.csv'):body='```csv\n'+body+'\n```'
        else:body=render(rel)
        chunks.append(f'<a id="{anchor}"></a>\n\n## 附錄：{Path(rel).name}\n\n'+body)
    chunks+=['## 教材授權\n\n'+(root/'LICENSE').read_text().strip()]
    return ('\n\n'.join(chunks)+'\n').encode()

def expected(root):
    m=load(root);version=m['version'];out={};entries=[]
    for e in m['entries']:
        pack=render_pack(root,e,version);out[e['pack']]=pack
        entries.append({**e,'sourceSha256':sha((root/e['source']).read_bytes()),'packSha256':sha(pack),
                        'referenceSha256':{p:sha((root/p).read_bytes()) for p in e['references']}})
    catalog={'schemaVersion':'2.0','edition':'free','version':version,'entryCount':len(entries),'entries':entries}
    if m.get('supplements'):
        catalog['supplements']=[]
        for e in m['supplements']:
            pack=render_supplement(root,e,version);out[e['pack']]=pack
            catalog['supplements'].append({**e,'sourceSha256':sha((root/e['source']).read_bytes()),'packSha256':sha(pack),'referenceSha256':{p:sha((root/p).read_bytes()) for p in e['references']}})
    out['catalog.json']=(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n').encode()
    intro=f'''# ThinkWithBlack 免費方法索引

教材版本：{version}｜共 {len(entries)} 份方法

## 先讀這段

本索引只用來選方法。每次使用者提問或換題，先選能完整處理當前工作的一份方法；回覆編號、名稱與下表的完整方法包路徑。還沒讀到該方法全文時，請使用者上傳後再執行，不用索引摘要代替方法

已讀同版本全文且題目相符時直接沿用；使用者補資料或修正時不要重問背景。換題需要另一方法時，回查本索引並要求該檔案。多項獨立工作先讓使用者指定一項；找不到適用方法就明說，不編造方法或檔名

先用本對話上傳的資料與指定可讀來源完成單項工作，交付後等待下一題。直接連接帳戶、整體診斷與自動接續、持續監測及外部系統操作，依 thinkwithblack-mcp 的產品服務處理

方法包已包含共用規則、全文、必要參考與授權

| 編號 | 方法 | 適用工作 | 上傳檔案 |
|---|---|---|---|
'''
    for e in entries:
        desc=e['description'].replace('|','／').replace('\n',' ')
        intro+=f'| {e["id"]} | {e["name"]} | {desc} | [{e["pack"]}]({e["pack"]}) |\n'
    if m.get('supplements'):
        intro+='\n## 附加校稿工具\n\n'
        for e in m['supplements']:intro+=f'- [{e["name"]}]({e["pack"]})：{e["description"]}\n'
    out['INDEX.md']=intro.encode()
    return m,out

def english_builder(root):
    return runpy.run_path(str(root/'scripts/build-english-edition.py'))

def verify(root):
    m,out=expected(root)
    en=english_builder(root)
    wanted=set(source_files(m))|set(out)|set(MAINTENANCE)|{'en/'+p for p in en['paths'](root)}
    actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts and '__pycache__' not in p.parts}
    if actual!=wanted:raise ValueError('File inventory mismatch: '+str(sorted(actual^wanted)))
    for rel,data in out.items():
        if (root/rel).read_bytes()!=data:raise ValueError('Stale generated file: '+rel)
    for rel in sorted(wanted):
        if any(x in Path(rel).parts for x in FORBIDDEN):raise ValueError('Forbidden product file: '+rel)
        t=(root/rel).read_text()
        if rel not in MAINTENANCE:
            for pat in PRODUCT_PATTERNS:
                if re.search(pat,t):raise ValueError('Product content in '+rel+': '+pat)
        if rel.endswith('.md'):
            for match in LINK.finditer(t):
                target=local_link(root,rel,match[1])
                if target and not target.is_file():raise ValueError('Broken local link in '+rel+': '+match[1])
                if (rel.startswith('packs/') or rel.startswith('en/packs/')) and target:raise ValueError('Pack has external file dependency: '+rel+': '+match[1])
    en['verify'](root)
    return m,out

def generate(root):
    m,out=expected(root)
    for rel,data in out.items():
        p=root/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    english_builder(root)['generate'](root)
    return m

def zip_bytes(root,paths,dest):
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for rel in sorted(paths):
            info=zipfile.ZipInfo(rel,date_time=(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            z.writestr(info,(root/rel).read_bytes())

def package(root,destination):
    m,out=verify(root);destination=destination.resolve()
    if destination.is_relative_to(root.resolve()):raise ValueError('Output directory must be outside the source repository')
    destination.mkdir(parents=True,exist_ok=True)
    en=english_builder(root);em,_=en['verify'](root);english_paths=en['paths'](root)
    content=sorted(set(source_files(m))|set(out)|{'en/'+p for p in english_paths});source=sorted(set(content)|set(MAINTENANCE))
    name='ThinkWithBlack-bilingual-'+em['version']
    receipt={'version':m['version'],'bundleVersion':em['version'],'entryCount':len(m['entries']),'files':{p:sha((root/p).read_bytes()) for p in content},'artifacts':{}}
    for suffix,paths in [('.zip',content),('-source.zip',source)]:
        target=destination/(name+suffix);zip_bytes(root,paths,target)
        receipt['artifacts'][target.name]={'sha256':sha(target.read_bytes()),'fileCount':len(paths)}
    target=destination/('ThinkWithBlack-free-en-'+em['version']+'.zip')
    zip_bytes(root/'en',english_paths,target)
    receipt['artifacts'][target.name]={'sha256':sha(target.read_bytes()),'fileCount':len(english_paths),'language':'en','version':em['version']}
    receipt['englishVersion']=em['version']
    (destination/(name+'-receipt.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    return receipt

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['generate','verify','package']);p.add_argument('--output',type=Path)
    a=p.parse_args()
    if a.action=='generate':m=generate(ROOT);print('Generated',len(m['entries']),'free packs')
    elif a.action=='verify':m,_=verify(ROOT);print('Verified',len(m['entries']),'free packs')
    else:
        if not a.output:p.error('--output is required')
        r=package(ROOT,a.output);print(json.dumps(r['artifacts'],indent=2))
