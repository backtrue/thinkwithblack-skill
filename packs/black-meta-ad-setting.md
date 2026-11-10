# Black 專屬 Meta 廣告投放流程

版本：2026.11.11-free.1｜原文語言：zh-TW

# black-meta-ad-setting

Black 專屬 Meta 廣告投放流程，版本 1.0，2026-11-02

## 任務入口

先確認本次要規劃、建立或啟用，以及指定帳戶、既有活動與企劃來源；沿用已提供資料與相符授權

- 從零規劃：先確認商品事實、USP、受眾假說、投放目標與成本邊界，再進入建立階段
- 已有核准企劃：直接核對資源及執行設定，不重跑商品、Persona 或文案製作
- 單獨圖片改版：接 `resize-ad-creatives`，交付指定比例後結束；不自行建立廣告
- 獨立使用：依下列八步執行，從環境取得必要的素材編輯及 Meta 帳戶工具；缺少必要工具或來源時列出具體缺件

只要求規劃時交付設定表，不寫入帳戶。要求建立時新建物件為 PAUSED；啟用與增加預算須有相符授權

執行順序：確認企劃 → 核對資源 → 準備素材 → Safe Zone → 受眾與版位 → 上稿 → 驗收 → 啟用與投遞確認。製作前先確認將使用的版位，上稿前核對素材及設定已配對

## 1. 確認企劃與操作範圍

以核准企劃為準，確認投放目標、商品、客群、地區、預算、排程、素材、文案、優惠、目的地與追蹤需求，保存企劃版本與來源位置

分清楚本次要沿用、建立或修改哪些活動、廣告組合與廣告，以及是否已授權啟用。已有資料直接沿用；真正缺少、會影響設定的決策才補問

**交付：一份可對照原企劃的投放設定表**

## 2. 核對帳戶與既有資源

實際確認廣告帳戶、幣別、時區、Facebook 粉專、Instagram 帳號、Pixel／資料集及使用的活動。需要沿用受眾、素材或貼文時，同時確認來源與使用權限

沿用廣告組合時，核對它是否屬於指定活動、是否符合本次目標。新建廣告組合依企劃重新設定，避免把舊組合中未經核對的受眾與版位設定一起帶入

預算須分清楚設在活動層或廣告組合層，並確認每日／總預算、幣別與排程時區

**交付：已核實的帳戶、投放層級與資源清單**

## 3. 準備多尺寸素材

新建圖片廣告至少準備兩種比例：

- 1:1＋9:16
- 或 4:5＋9:16
- 完整素材組優先備齊 1:1、4:5、9:16

可採用的製作畫布為 1080×1080、1080×1350、1080×1920，實際交付時核對檔案像素與比例

收到單一尺寸時，先完成缺少版本的改版。改版須依比例重新安排商品、標題、價格與裝飾，保留商品外觀、品牌、文字、數量、幣別與優惠條件

原圖另存保留，各比例使用清楚的新檔名。若指定沿用既有貼文並保留互動，維持原貼文與素材；新製素材另依企劃處理

**交付：多尺寸正式圖片與素材清單**

## 4. 製作與檢查 Safe Zone

Safe Zone 是放置重要資訊的安全區，目的是讓商品、品牌、文字與優惠避開版位裁切及介面遮擋

製作 9:16 圖片前，分別核對 Stories 與 Reels 當次適用的官方圖片規格或已確認模板，記錄來源、日期與安全區範圍。共用一張圖時，採兩個版位安全區的交集；容納不下時，分開製作

商品辨識主體、品牌標誌、主標、價格與優惠條件都要放進安全區，避開頂端帳號列、右側互動按鈕與底部說明及行動按鈕。背景與裝飾可延伸滿版

產圖後逐張開啟檢查：

- 文字、價格、數量、幣別與原圖一致
- 商品、標誌與包裝細節正確
- 重要元素完整落在 Safe Zone 內
- 縮小至手機觀看大小仍可閱讀

AI 提示詞寫了 Safe Zone，成品仍須實際檢查；發現遮擋或變形就修正並重看

**交付：乾淨正式圖、使用同一成品疊加標示的 Safe Zone 檢查圖，以及素材×版位對照表**

## 5. 設定受眾、出價與版位

既有廣告組合需要修改時，依相符授權處理；帳戶層控制另核對影響範圍

受眾、地區、年齡、性別、排除條件、最佳化目標與轉換事件依核准企劃設定。需要嚴格測試的受眾條件，確認後台實際採用的是限制還是擴張建議

地點設定依既有上稿規範，固定使用「居住或最近位於此地」的合併設定。透過 API 建立時，在 `geo_locations` 明確填入 `location_types: ["home", "recent"]`，國家、城市或區域則依核准企劃設定

不得只填 `home`、只填 `recent`、使用 `travel_in` 或舊版 Location Type，也不得省略 `location_types`。沿用既有廣告組合時，同樣讀回核對這個欄位

本流程的版位操作標準如下：

| 項目 | 操作規則 | 核對方式 |
|---|---|---|
| Audience Network 出價 | 套用出價降低 90% 的值規則 | 確認條件、實際幅度與廣告組合套用結果 |
| Audience Network 版位 | 在廣告投放設定的「版位控制項」取消勾選 | 確認儲存後的排除設定與作用範圍 |
| Marketplace | 建議取消，依本次核准選擇執行 | 讀回實際設定 |
| 右側欄 | 建議取消，依本次核准選擇執行 | 讀回實際設定 |
| Stories／Reels | 依投放需求選擇 | 確認有對應素材及可用預覽 |

Audience Network 的出價調整與版位排除要分開檢查，兩項都保留證據。值規則名稱不能代替實際幅度；沿用既有組合時也要核對，不只在新建時設定

若需要修改帳戶層控制項，先確認會影響哪些廣告及本次授權範圍。工具缺少設定能力時，透過已授權的後台介面完成

**交付：受眾、出價、版位及作用範圍的設定紀錄**

## 6. 依版位建立素材與廣告

建立素材時，依版位上傳對應版本：動態消息使用本次選定的 1:1 或 4:5；Stories／Reels 使用通過 Safe Zone 檢查的 9:16。逐一確認後台實際配對的圖片

按企劃填入主要文案、標題、描述、CTA、目的地與追蹤參數，核對 Facebook 與 Instagram 顯示身分。保留原文與優惠，不在上稿途中自行改寫

沿用既有貼文時核對原貼文 ID 與內容，確保保留指定貼文。建立前先查重，已建立且符合要求的物件直接記錄，避免重複上稿

新建物件預設為暫停（PAUSED），建立後立即保存 ID 與實際狀態。操作中斷或結果不明時，先查現況再決定是否重送

**交付：已建立的廣告清單、素材配置與物件 ID**

## 7. 上線前讀回與預覽驗收

儲存後重新開啟設定，逐項比對「企劃要求 → 實際儲存值 → 證據 → 結果」

必要核對項目：

- 帳戶、活動與廣告組合歸屬
- 預算、排程、時區、受眾及排除條件
- 地點範圍符合企劃，且 `geo_locations.location_types` 同時包含 `home` 與 `recent`
- 出價、版位、Pixel／資料集與轉換事件
- Facebook／Instagram 身分
- 文案、素材版本、原貼文 ID、CTA、網址與追蹤參數
- 物件狀態與平台顯示的錯誤

逐版位打開實際預覽，檢查圖片配對、裁切、Safe Zone、介面遮擋與可讀性。圖片檔案檢查與後台預覽分開記錄

發現不符就修正並重新驗收；必要設定讀不到或預覽尚未取得時，列出具體待核對項目，維持草稿／暫停

**交付：逐項驗收表、各版位預覽與待處理清單**

## 8. 啟用與投放確認

必要驗收通過，且已有本批明確啟用授權後，依授權範圍啟用。已取得的相符授權直接沿用；需要額外啟用父層或增加預算時，核對是否包含在授權內

啟用後讀回活動、廣告組合及廣告狀態，確認審核、排程、錯誤與實際投遞情況

回報時清楚區分：已建立、驗收完成、已啟用、審核／處理中、已有投遞。要確認開始投放，需查看實際投遞、曝光或花費資料

**交付：啟用物件、實際狀態、投遞證據與需要追蹤的事項**

## 每批固定保留的交付資料

| 文件 | 內容 |
|---|---|
| 投放設定表 | 企劃版本、目標、帳戶、預算、受眾、版位、排程與授權範圍 |
| 素材×版位表 | 檔名、像素、比例、使用版位、Safe Zone 來源與檢查結果 |
| 上稿與驗收表 | 各層物件 ID、實際設定、逐版位預覽、核對結果與待辦 |
| 啟用紀錄 | 啟用範圍、時間、讀回狀態及實際投遞證據 |


## 階段與證據交接

規劃階段交付投放設定表與尚待決定項目，沒有實際帳戶資料時仍可完成可支持的規劃，不宣稱已建立

建立階段需要指定企劃與素材來源、已查證的帳戶及活動範圍，以及使用者原話所支持的建立授權；只建立 PAUSED 物件

上稿交付需要逐欄讀回、逐版位預覽、物件 ID、實際狀態及待核對清單的證據；有缺件時如實標示部分完成

啟用階段需要已通過的必要 QA、具體物件與父層狀態，以及使用者原話所支持的啟用授權；建立授權不能代替啟用授權

啟用交付需要實際狀態讀回，只有另取得曝光或花費證據才標示已有投遞

<a id="supplement-reference-1"></a>

## 附錄：context-contract.json

{
  "skill_id": "references/lecture-skills/black-meta-ad-setting/SKILL.md",
  "source_sha256": "c53f1e84f3cb1307ca71ccf6862ffd502299ffafc554e96553a35ac389da8374",
  "role": "unneeded",
  "stages": {
    "start": {
      "requires": {
        "all": []
      },
      "delivery": false,
      "allowed_output": "\u5224\u5225\u7bc4\u570d\uff0c\u55ae\u6539\u5716\u4ea4\u7d66 resize-ad-creatives"
    },
    "analyze": {
      "requires": {
        "all": [
          {
            "field": "task.ad_job",
            "label": "\u672c\u6b21\u4efb\u52d9\u8207\u7bc4\u570d",
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
            "source_excerpt": "\u5148\u78ba\u8a8d\u672c\u6b21\u8981\u898f\u5283\u3001\u5efa\u7acb\u6216\u555f\u7528\uff0c\u4ee5\u53ca\u6307\u5b9a\u5e33\u6236\u3001\u65e2\u6709\u6d3b\u52d5\u8207\u4f01\u5283\u4f86\u6e90\uff1b\u6cbf\u7528\u5df2\u63d0\u4f9b\u8cc7\u6599\u8207\u76f8\u7b26\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": false,
      "allowed_output": "\u4f9d\u5df2\u77e5\u8cc7\u6599\u898f\u5283\u4e26\u5217\u7f3a\u4ef6\uff0c\u4e0d\u5beb\u5165\u5e33\u6236"
    },
    "plan": {
      "requires": {
        "all": [
          {
            "field": "task.ad_job",
            "label": "\u672c\u6b21\u4efb\u52d9\u8207\u7bc4\u570d",
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
            "source_excerpt": "\u5148\u78ba\u8a8d\u672c\u6b21\u8981\u898f\u5283\u3001\u5efa\u7acb\u6216\u555f\u7528\uff0c\u4ee5\u53ca\u6307\u5b9a\u5e33\u6236\u3001\u65e2\u6709\u6d3b\u52d5\u8207\u4f01\u5283\u4f86\u6e90\uff1b\u6cbf\u7528\u5df2\u63d0\u4f9b\u8cc7\u6599\u8207\u76f8\u7b26\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.ad_plan",
            "label": "\u6295\u653e\u898f\u5283\u8207\u7f3a\u4ef6",
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
            "source_line": 156,
            "source_excerpt": "\u898f\u5283\u968e\u6bb5\u4ea4\u4ed8\u6295\u653e\u8a2d\u5b9a\u8868\u8207\u5c1a\u5f85\u6c7a\u5b9a\u9805\u76ee\uff0c\u6c92\u6709\u5be6\u969b\u5e33\u6236\u8cc7\u6599\u6642\u4ecd\u53ef\u5b8c\u6210\u53ef\u652f\u6301\u7684\u898f\u5283\uff0c\u4e0d\u5ba3\u7a31\u5df2\u5efa\u7acb",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": true,
      "allowed_output": "\u4ea4\u4ed8\u6295\u653e\u8a2d\u5b9a\u8868\u8207\u7f3a\u4ef6\uff0c\u4e0d\u5ba3\u7a31\u5df2\u5efa\u7acb"
    },
    "execute": {
      "requires": {
        "all": [
          {
            "field": "task.ad_job",
            "label": "\u672c\u6b21\u4efb\u52d9\u8207\u7bc4\u570d",
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
            "source_excerpt": "\u5148\u78ba\u8a8d\u672c\u6b21\u8981\u898f\u5283\u3001\u5efa\u7acb\u6216\u555f\u7528\uff0c\u4ee5\u53ca\u6307\u5b9a\u5e33\u6236\u3001\u65e2\u6709\u6d3b\u52d5\u8207\u4f01\u5283\u4f86\u6e90\uff1b\u6cbf\u7528\u5df2\u63d0\u4f9b\u8cc7\u6599\u8207\u76f8\u7b26\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.upload_plan",
            "label": "\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90",
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
            "source_line": 158,
            "source_excerpt": "\u5efa\u7acb\u968e\u6bb5\u9700\u8981\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90\u3001\u5df2\u67e5\u8b49\u7684\u5e33\u6236\u53ca\u6d3b\u52d5\u7bc4\u570d\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u5efa\u7acb\u6388\u6b0a\uff1b\u53ea\u5efa\u7acb PAUSED \u7269\u4ef6",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.upload_scope",
            "label": "\u5df2\u67e5\u8b49\u5e33\u6236\u6d3b\u52d5\u7bc4\u570d",
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
            "source_line": 158,
            "source_excerpt": "\u5efa\u7acb\u968e\u6bb5\u9700\u8981\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90\u3001\u5df2\u67e5\u8b49\u7684\u5e33\u6236\u53ca\u6d3b\u52d5\u7bc4\u570d\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u5efa\u7acb\u6388\u6b0a\uff1b\u53ea\u5efa\u7acb PAUSED \u7269\u4ef6",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.upload_authorization",
            "label": "\u5efa\u7acb\u6388\u6b0a\u539f\u8a71",
            "location": "task",
            "states": [
              "user_confirmed"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 158,
            "source_excerpt": "\u5efa\u7acb\u968e\u6bb5\u9700\u8981\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90\u3001\u5df2\u67e5\u8b49\u7684\u5e33\u6236\u53ca\u6d3b\u52d5\u7bc4\u570d\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u5efa\u7acb\u6388\u6b0a\uff1b\u53ea\u5efa\u7acb PAUSED \u7269\u4ef6",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": false,
      "allowed_output": "\u57f7\u884c\u6388\u6b0a PAUSED \u5efa\u7acb\u53ca\u8b80\u56de"
    },
    "deliver": {
      "requires": {
        "all": [
          {
            "field": "task.ad_job",
            "label": "\u672c\u6b21\u4efb\u52d9\u8207\u7bc4\u570d",
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
            "source_excerpt": "\u5148\u78ba\u8a8d\u672c\u6b21\u8981\u898f\u5283\u3001\u5efa\u7acb\u6216\u555f\u7528\uff0c\u4ee5\u53ca\u6307\u5b9a\u5e33\u6236\u3001\u65e2\u6709\u6d3b\u52d5\u8207\u4f01\u5283\u4f86\u6e90\uff1b\u6cbf\u7528\u5df2\u63d0\u4f9b\u8cc7\u6599\u8207\u76f8\u7b26\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.upload_plan",
            "label": "\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90",
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
            "source_line": 158,
            "source_excerpt": "\u5efa\u7acb\u968e\u6bb5\u9700\u8981\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90\u3001\u5df2\u67e5\u8b49\u7684\u5e33\u6236\u53ca\u6d3b\u52d5\u7bc4\u570d\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u5efa\u7acb\u6388\u6b0a\uff1b\u53ea\u5efa\u7acb PAUSED \u7269\u4ef6",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.upload_scope",
            "label": "\u5df2\u67e5\u8b49\u5e33\u6236\u6d3b\u52d5\u7bc4\u570d",
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
            "source_line": 158,
            "source_excerpt": "\u5efa\u7acb\u968e\u6bb5\u9700\u8981\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90\u3001\u5df2\u67e5\u8b49\u7684\u5e33\u6236\u53ca\u6d3b\u52d5\u7bc4\u570d\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u5efa\u7acb\u6388\u6b0a\uff1b\u53ea\u5efa\u7acb PAUSED \u7269\u4ef6",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.upload_authorization",
            "label": "\u5efa\u7acb\u6388\u6b0a\u539f\u8a71",
            "location": "task",
            "states": [
              "user_confirmed"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 158,
            "source_excerpt": "\u5efa\u7acb\u968e\u6bb5\u9700\u8981\u6307\u5b9a\u4f01\u5283\u8207\u7d20\u6750\u4f86\u6e90\u3001\u5df2\u67e5\u8b49\u7684\u5e33\u6236\u53ca\u6d3b\u52d5\u7bc4\u570d\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u5efa\u7acb\u6388\u6b0a\uff1b\u53ea\u5efa\u7acb PAUSED \u7269\u4ef6",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.upload_readback",
            "label": "\u9010\u6b04\u8b80\u56de\u8207\u9810\u89bd\u8b49\u64da",
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
            "source_line": 160,
            "source_excerpt": "\u4e0a\u7a3f\u4ea4\u4ed8\u9700\u8981\u9010\u6b04\u8b80\u56de\u3001\u9010\u7248\u4f4d\u9810\u89bd\u3001\u7269\u4ef6 ID\u3001\u5be6\u969b\u72c0\u614b\u53ca\u5f85\u6838\u5c0d\u6e05\u55ae\u7684\u8b49\u64da\uff1b\u6709\u7f3a\u4ef6\u6642\u5982\u5be6\u6a19\u793a\u90e8\u5206\u5b8c\u6210",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": true,
      "allowed_output": "\u4f9d\u5be6\u969b\u9a57\u6536\u8b49\u64da\u4ea4\u4ed8\u4e0a\u7a3f\u7d50\u679c\u53ca\u7f3a\u4ef6"
    },
    "activate": {
      "requires": {
        "all": [
          {
            "field": "task.ad_job",
            "label": "\u672c\u6b21\u4efb\u52d9\u8207\u7bc4\u570d",
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
            "source_excerpt": "\u5148\u78ba\u8a8d\u672c\u6b21\u8981\u898f\u5283\u3001\u5efa\u7acb\u6216\u555f\u7528\uff0c\u4ee5\u53ca\u6307\u5b9a\u5e33\u6236\u3001\u65e2\u6709\u6d3b\u52d5\u8207\u4f01\u5283\u4f86\u6e90\uff1b\u6cbf\u7528\u5df2\u63d0\u4f9b\u8cc7\u6599\u8207\u76f8\u7b26\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.activation_qa",
            "label": "\u5fc5\u8981QA\u901a\u904e\u53ca\u7269\u4ef6\u7236\u5c64\u72c0\u614b",
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
            "source_line": 162,
            "source_excerpt": "\u555f\u7528\u968e\u6bb5\u9700\u8981\u5df2\u901a\u904e\u7684\u5fc5\u8981 QA\u3001\u5177\u9ad4\u7269\u4ef6\u8207\u7236\u5c64\u72c0\u614b\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u555f\u7528\u6388\u6b0a\uff1b\u5efa\u7acb\u6388\u6b0a\u4e0d\u80fd\u4ee3\u66ff\u555f\u7528\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.activation_authorization",
            "label": "\u555f\u7528\u6388\u6b0a\u539f\u8a71",
            "location": "task",
            "states": [
              "user_confirmed"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 162,
            "source_excerpt": "\u555f\u7528\u968e\u6bb5\u9700\u8981\u5df2\u901a\u904e\u7684\u5fc5\u8981 QA\u3001\u5177\u9ad4\u7269\u4ef6\u8207\u7236\u5c64\u72c0\u614b\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u555f\u7528\u6388\u6b0a\uff1b\u5efa\u7acb\u6388\u6b0a\u4e0d\u80fd\u4ee3\u66ff\u555f\u7528\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": false,
      "allowed_output": "\u5c0d\u6307\u5b9a\u4e14QA\u901a\u904e\u7684\u7269\u4ef6\u555f\u7528"
    },
    "activated": {
      "requires": {
        "all": [
          {
            "field": "task.ad_job",
            "label": "\u672c\u6b21\u4efb\u52d9\u8207\u7bc4\u570d",
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
            "source_excerpt": "\u5148\u78ba\u8a8d\u672c\u6b21\u8981\u898f\u5283\u3001\u5efa\u7acb\u6216\u555f\u7528\uff0c\u4ee5\u53ca\u6307\u5b9a\u5e33\u6236\u3001\u65e2\u6709\u6d3b\u52d5\u8207\u4f01\u5283\u4f86\u6e90\uff1b\u6cbf\u7528\u5df2\u63d0\u4f9b\u8cc7\u6599\u8207\u76f8\u7b26\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.activation_qa",
            "label": "\u5fc5\u8981QA\u901a\u904e\u53ca\u7269\u4ef6\u7236\u5c64\u72c0\u614b",
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
            "source_line": 162,
            "source_excerpt": "\u555f\u7528\u968e\u6bb5\u9700\u8981\u5df2\u901a\u904e\u7684\u5fc5\u8981 QA\u3001\u5177\u9ad4\u7269\u4ef6\u8207\u7236\u5c64\u72c0\u614b\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u555f\u7528\u6388\u6b0a\uff1b\u5efa\u7acb\u6388\u6b0a\u4e0d\u80fd\u4ee3\u66ff\u555f\u7528\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.activation_authorization",
            "label": "\u555f\u7528\u6388\u6b0a\u539f\u8a71",
            "location": "task",
            "states": [
              "user_confirmed"
            ],
            "value_types": [
              "text",
              "texts",
              "references"
            ],
            "scope": [],
            "min_count": 1,
            "source_line": 162,
            "source_excerpt": "\u555f\u7528\u968e\u6bb5\u9700\u8981\u5df2\u901a\u904e\u7684\u5fc5\u8981 QA\u3001\u5177\u9ad4\u7269\u4ef6\u8207\u7236\u5c64\u72c0\u614b\uff0c\u4ee5\u53ca\u4f7f\u7528\u8005\u539f\u8a71\u6240\u652f\u6301\u7684\u555f\u7528\u6388\u6b0a\uff1b\u5efa\u7acb\u6388\u6b0a\u4e0d\u80fd\u4ee3\u66ff\u555f\u7528\u6388\u6b0a",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          },
          {
            "field": "task.activation_readback",
            "label": "\u555f\u7528\u5f8c\u72c0\u614b\u8b80\u56de",
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
            "source_line": 164,
            "source_excerpt": "\u555f\u7528\u4ea4\u4ed8\u9700\u8981\u5be6\u969b\u72c0\u614b\u8b80\u56de\uff0c\u53ea\u6709\u53e6\u53d6\u5f97\u66dd\u5149\u6216\u82b1\u8cbb\u8b49\u64da\u624d\u6a19\u793a\u5df2\u6709\u6295\u905e",
            "missing_action": "collect_authorized_source",
            "preparation": null,
            "condition": null
          }
        ]
      },
      "delivery": true,
      "allowed_output": "\u4ea4\u4ed8\u555f\u7528\u5f8c\u5be6\u969b\u72c0\u614b\uff1b\u6295\u905e\u53e6\u9700\u66dd\u5149\u82b1\u8cbb\u8b49\u64da"
    }
  },
  "writeback": [],
  "invalidation": {
    "fields": [],
    "dependents": "\u4f01\u5283\u3001\u7d20\u6750\u3001\u7248\u4f4d\u6216\u6388\u6b0a\u6539\u8b8a\u6642\u91cd\u6838\u76f8\u4f9d\u7522\u7269"
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
  "method_sha256": "c53f1e84f3cb1307ca71ccf6862ffd502299ffafc554e96553a35ac389da8374",
  "method_path": "supplements/black-meta-ad-setting/SKILL.md",
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
