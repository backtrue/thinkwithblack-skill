# 廣告素材多尺寸改版

版本：2026.11.11-free.1｜原文語言：zh-TW

# 廣告素材多尺寸改版

將使用者提供的廣告原圖改成可供指定版位使用的圖片，保留商品、品牌與優惠資訊，依比例重新安排構圖

## 輸入與尺寸

- 先實際開啟原圖，讀取檔案尺寸，逐字記錄主標、價格、原價、數量、優惠條件與品牌標誌，辨識商品外觀及包裝
- 沿用對話已指定的版位與比例。只要求一個版本就做該版本，例如「轉成 9:16」不自動增加其他比例
- 要求完整廣告尺寸組時，至少提供 1:1＋9:16 或 4:5＋9:16，優先備齊三種比例；依已知投放版位選擇，缺少比例選擇且無其他線索時採三種
- 畫布範例為 1080×1080、1080×1350、1080×1920；實際輸出必須核對像素與比例，生成工具不支援指定大小時，先使用可用的同比例尺寸並記錄
- 原始檔另存保留，輸出使用新檔名

## 版位安全區

製作 Stories 或 Reels 前，讀取當次官方規格或使用者提供的版位模板，記錄平台、版位、圖片格式、查核日期、來源連結與安全區範圍。Stories 與 Reels 分別核對，不把某次百分比寫成永久通則

查核可由 Meta Ads Guide 對應頁開始：
- https://www.facebook.com/business/ads-guide/image/instagram-story
- https://www.facebook.com/business/ads-guide/image/instagram-reels

依實際讀到的圖片規格決定邊界，影片規格不直接代替圖片規格。來源無法讀取時，可依使用者模板或明示的製作留白先做預覽，記錄待核對版位

把安全區轉成實際畫布座標，以左上角為原點。若左右上下保留比例為 L、R、T、B，安全矩形為 x=[L×W,(1−R)×W]、y=[T×H,(1−B)×H]

同一張供多版位使用時，取各安全區交集，並避開右側互動按鈕、上方帳號列與下方說明及行動按鈕。商品辨識主體、標誌、主標、價格及優惠條件須完整落在其中；背景、格線、裝飾可延伸滿版

空間不足時重新分配商品與文字大小、換行及間距；仍無法兼顧可讀性時分別製作版位版本

## 圖片製作

使用可用的 imagegen 圖片編輯工具；本機原圖先開啟檢視，再作為編輯來源。需要工具操作指引時讀取環境中的 imagegen Skill

提示詞必須包含：
- 原圖是編輯對象，以及要保留的商品包裝、標誌、配色與視覺風格
- 目標比例、像素與文字逐字清單
- 安全區實際座標或比例，以及標題、商品、價格各自的預計區域
- 背景延伸與重新排版要求
- 正式圖保持乾淨，不含安全區線、平台介面或浮水印

保留商品形狀、標誌、包裝文字與顏色，不能生成另一款商品。保持價格、數量與優惠語意，原文「單片 $33」即原樣保留，不因自行計算而改價。不自行增加優惠、CTA 或功效宣稱

不得只把橫圖拉長、裁掉資訊或依賴上稿端自動裁切。重排商品、文字與裝飾，確保實際手機觀看時可讀

## 產圖後檢查與修正

每個版本產出後重新開啟實際圖片，檢查：
1. 像素尺寸與目標比例相符
2. 每段文字、數字、幣別、數量與原圖一致，沒有漏字或錯字
3. 商品與標誌保持原貌，包裝沒有新增、變形或錯置的細節
4. 所有重要元素的實際邊界落在安全區內，尤其是價格、原價與角落徽章
5. 縮小到手機顯示大小後，主標、商品與價格仍清楚

提示詞要求留白不等於成品已符合。若價格仍落在下方介面區，針對實際問題移動或縮整組內容，再次開啟結果檢查；保留上一版供比對

同時輸出乾淨正式圖與安全區檢查圖。檢查圖使用與正式圖相同的圖片內容及像素尺寸，另加安全區邊框、遮擋區與版位標示；不得為了畫框重生成商品及文案。可用 SVG 外層引用正式圖疊加框線，作為獨立檢查檔；不得用 SVG 代替正式廣告圖片

## 交付與上稿交接

展示正式圖，附可開啟的檔案與安全區檢查圖。提供簡短對照表：檔名、實際像素、比例、適用版位、安全區來源／製作假設、圖片檢查結果

上稿流程接收成品後，依版位上傳對應尺寸，並檢查實際廣告預覽。素材檔案檢查與後台預覽分開記錄

沿用既有 Hero 多圖貼文且使用者指定不改素材時，保留原貼文與素材；新建圖片廣告依本 Skill 製作。值規則、受眾、預算、版位開關與廣告發布交由上稿流程處理

<a id="supplement-reference-1"></a>

## 附錄：context-contract.json

{
  "skill_id": "references/lecture-skills/resize-ad-creatives/SKILL.md",
  "source_sha256": "488520dba7686aeb390920e6b5ae497ddb3f07977ef642ec1748bdde42c7f20a",
  "role": "unneeded",
  "stages": {
    "execute": {
      "requires": {
        "all": [
          {
            "field": "task.creatives",
            "label": "\u539f\u5716\u8207\u9010\u5b57\u8cc7\u8a0a",
            "location": "task",
            "states": [
              "source_stated",
              "user_confirmed",
              "data_supported"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 12,
            "source_excerpt": "- \u5148\u5be6\u969b\u958b\u555f\u539f\u5716\uff0c\u8b80\u53d6\u6a94\u6848\u5c3a\u5bf8\uff0c\u9010\u5b57\u8a18\u9304\u4e3b\u6a19\u3001\u50f9\u683c\u3001\u539f\u50f9\u3001\u6578\u91cf\u3001\u512a\u60e0\u689d\u4ef6\u8207\u54c1\u724c\u6a19\u8a8c\uff0c\u8fa8\u8b58\u5546\u54c1\u5916\u89c0\u53ca\u5305\u88dd",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.placement_job",
            "label": "\u6307\u5b9a\u6bd4\u4f8b\u8207\u4f7f\u7528\u7248\u4f4d",
            "location": "task",
            "states": [
              "source_stated",
              "user_confirmed",
              "data_supported"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 13,
            "source_excerpt": "- \u6cbf\u7528\u5c0d\u8a71\u5df2\u6307\u5b9a\u7684\u7248\u4f4d\u8207\u6bd4\u4f8b\u3002\u53ea\u8981\u6c42\u4e00\u500b\u7248\u672c\u5c31\u505a\u8a72\u7248\u672c\uff0c\u4f8b\u5982\u300c\u8f49\u6210 9:16\u300d\u4e0d\u81ea\u52d5\u589e\u52a0\u5176\u4ed6\u6bd4\u4f8b",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": false,
      "allowed_output": "\u4f9d\u539f\u5716\u53ca\u76ee\u6a19\u6bd4\u4f8b\u5b8c\u6210\u6539\u7248\u4e26\u6aa2\u67e5\u5b89\u5168\u5340"
    },
    "deliver": {
      "requires": {
        "all": [
          {
            "field": "task.creatives",
            "label": "\u539f\u5716\u8207\u9010\u5b57\u8cc7\u8a0a",
            "location": "task",
            "states": [
              "source_stated",
              "user_confirmed",
              "data_supported"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 12,
            "source_excerpt": "- \u5148\u5be6\u969b\u958b\u555f\u539f\u5716\uff0c\u8b80\u53d6\u6a94\u6848\u5c3a\u5bf8\uff0c\u9010\u5b57\u8a18\u9304\u4e3b\u6a19\u3001\u50f9\u683c\u3001\u539f\u50f9\u3001\u6578\u91cf\u3001\u512a\u60e0\u689d\u4ef6\u8207\u54c1\u724c\u6a19\u8a8c\uff0c\u8fa8\u8b58\u5546\u54c1\u5916\u89c0\u53ca\u5305\u88dd",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.placement_job",
            "label": "\u6307\u5b9a\u6bd4\u4f8b\u8207\u4f7f\u7528\u7248\u4f4d",
            "location": "task",
            "states": [
              "source_stated",
              "user_confirmed",
              "data_supported"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 13,
            "source_excerpt": "- \u6cbf\u7528\u5c0d\u8a71\u5df2\u6307\u5b9a\u7684\u7248\u4f4d\u8207\u6bd4\u4f8b\u3002\u53ea\u8981\u6c42\u4e00\u500b\u7248\u672c\u5c31\u505a\u8a72\u7248\u672c\uff0c\u4f8b\u5982\u300c\u8f49\u6210 9:16\u300d\u4e0d\u81ea\u52d5\u589e\u52a0\u5176\u4ed6\u6bd4\u4f8b",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.creative_outputs",
            "label": "\u6b63\u5f0f\u5716\u8207\u5b89\u5168\u5340\u6aa2\u67e5\u5716",
            "location": "task",
            "states": [
              "data_supported"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 60,
            "source_excerpt": "\u540c\u6642\u8f38\u51fa\u4e7e\u6de8\u6b63\u5f0f\u5716\u8207\u5b89\u5168\u5340\u6aa2\u67e5\u5716\u3002\u6aa2\u67e5\u5716\u4f7f\u7528\u8207\u6b63\u5f0f\u5716\u76f8\u540c\u7684\u5716\u7247\u5167\u5bb9\u53ca\u50cf\u7d20\u5c3a\u5bf8\uff0c\u53e6\u52a0\u5b89\u5168\u5340\u908a\u6846\u3001\u906e\u64cb\u5340\u8207\u7248\u4f4d\u6a19\u793a\uff1b\u4e0d\u5f97\u70ba\u4e86\u756b\u6846\u91cd\u751f\u6210\u5546\u54c1\u53ca\u6587\u6848\u3002\u53ef\u7528 SVG \u5916\u5c64\u5f15\u7528\u6b63\u5f0f\u5716\u758a\u52a0\u6846\u7dda\uff0c\u4f5c\u70ba\u7368\u7acb\u6aa2\u67e5\u6a94\uff1b\u4e0d\u5f97\u7528 SVG \u4ee3\u66ff\u6b63\u5f0f\u5ee3\u544a\u5716\u7247",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.creative_review",
            "label": "\u7522\u5716\u5f8c\u5be6\u969b\u6aa2\u67e5\u7d00\u9304",
            "location": "task",
            "states": [
              "data_supported"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 51,
            "source_excerpt": "\u6bcf\u500b\u7248\u672c\u7522\u51fa\u5f8c\u91cd\u65b0\u958b\u555f\u5be6\u969b\u5716\u7247\uff0c\u6aa2\u67e5\uff1a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": true,
      "allowed_output": "\u4ea4\u4ed8\u6b63\u5f0f\u5716\u3001\u5b89\u5168\u5340\u6aa2\u67e5\u5716\u8207\u5c3a\u5bf8\u5c0d\u7167\u8868"
    }
  },
  "writeback": [],
  "invalidation": {
    "fields": [],
    "dependents": "\u4f86\u6e90\u5716\u7247\u3001\u7248\u4f4d\u8981\u6c42\u6216\u4f01\u5283\u6539\u8b8a\u6642\u91cd\u6838\u76f8\u95dc\u7522\u7269"
  },
  "social_evidence": {
    "schema_version": 1,
    "applies_to": "social_evidence_only",
    "account_confirmation_required": true,
    "content_review_required": true,
    "source_revision_required": true,
    "founder_and_brand_separate": true,
    "provider_persona_inference_state": "hypothesis",
    "company_identity_from_social": false,
    "missing_action": "discover_confirm_collect_review_sources",
    "raw_content": "read_selected_evidence_on_demand",
    "workflow": [
      "discover_accounts_and_preview",
      "confirm_account_relationship_and_usage",
      "collect_relevant_original_content",
      "show_extracted_fields_with_sources",
      "confirm_selected_facts_then_writeback"
    ],
    "snapshot_fields": {
      "source_accounts": [
        "id",
        "platform",
        "url",
        "platform_id (optional)",
        "revision",
        "status=confirmed",
        "relationship",
        "usage",
        "confirmation",
        "confirmed_identity_sha256"
      ],
      "source_reviews": [
        "id",
        "status=approved",
        "source_revisions",
        "confirmation",
        "evidence_sha256"
      ],
      "evidence.social": [
        "source_id",
        "collection_id",
        "platform",
        "platform_content_id",
        "content_kind",
        "source_revision",
        "coverage",
        "review_id"
      ]
    },
    "identity_digest": "sha256 of canonical JSON {platform,identity:platform_id or url}",
    "confirmation_evidence": "Original conversation or approved_document excerpt, source, retrieved_at, brand scope and sha256 of the excerpt",
    "coverage_requirements": {
      "metadata_only": "video_description",
      "transcript": "transcript with language, origin and start/end timecodes",
      "audiovisual": "audiovisual_analysis with reader, audio/visual modes, timecodes and receipt",
      "video_body": [
        "transcript",
        "audiovisual"
      ]
    },
    "search_candidates": "Host searches and reads original discovery evidence, then calls brand_sources_add; candidate still needs user confirmation",
    "review_evidence_digest": "sha256 of the approved full evidence JSON with recursively sorted object keys; task evidence must match the approved digest",
    "policy_sha256": "0d459af1d6903ed822d51764268ae42d85ce5c452b03093b7d84f4b42fe29a69",
    "field_requirements": []
  },
  "schema_version": 1,
  "method_sha256": "488520dba7686aeb390920e6b5ae497ddb3f07977ef642ec1748bdde42c7f20a",
  "method_path": "supplements/resize-ad-creatives/SKILL.md",
  "source_language": "zh-TW",
  "source_note": "Source excerpts preserve the reviewed method language; structured checks are shared across editions."
}

<a id="supplement-reference-2"></a>

## 附錄：check-context.py

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
