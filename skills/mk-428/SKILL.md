---
name: mk-428
description: "UTM 網址產生與檢查。用於需要可追蹤網址與參數錯誤的工作；依本項方法處理已指定資料並核對交付"
---

# MK-428｜UTM 網址產生與檢查

一般對話請上傳 `packs/mk-428.md`，其中已包含共用規則、本文及必要參考

## 工作目的

這個技能交付：**可追蹤網址與參數錯誤**

跨平台曝光相加不是去重觸及；不同歸因窗的轉換不能直接當全站真實訂單相加

## 必要資料

請提供：完整目的 URL、核准的 source/medium/campaign 值、需要時的 content/term、現有追蹤參數及需要保留的 query 與 fragment

## 方法步驟

1. 拆分目的 URL 的路徑、既有 query 與 fragment，保留非 UTM 參數
2. 依核准字典補 source、medium、campaign 與必要選填值，將值做 URL 編碼；同一 UTM 鍵已有不同值時指出衝突，使用已確認值而非重複追加
3. 重組時 query 放在 fragment 前，解碼讀回每個值，檢查原有參數與 fragment 未遺失
4. 交完整 URL 與參數表；只有實際測試及分析工具讀回後才標記收到預期來源

## 計算與判讀

參數值依已核准命名保留大小寫，特殊字元需編碼；網址正確與 GA4 已收資料分開核對

來源：[Google Analytics：自訂網址參數](https://support.google.com/analytics/answer/10917952?hl=en)

## 固定交付欄位

| 順序 | 欄位 | 填寫方式 |
|---:|---|---|
| 1 | 完整原始 URL | 填入已提供來源、計算或明確未知 |
| 2 | 核准 UTM 值 | 填入已提供來源、計算或明確未知 |
| 3 | 現有參數及衝突 | 填入已提供來源、計算或明確未知 |
| 4 | 完整產出 URL | 填入已提供來源、計算或明確未知 |
| 5 | 解碼讀回 | 填入已提供來源、計算或明確未知 |
| 6 | 原參數與 fragment 核對 | 填入已提供來源、計算或明確未知 |
| 7 | 實際測試狀態 | 填入已提供來源、計算或明確未知 |

## 核對案例

**MK-428-A1｜目的頁帶 ?sku=1#details，campaign 有空白**

預期：保留 sku 與 #details，將 UTM query 放在 fragment 前並編碼讀回

## 方法來源

原始檔：營業額提升主要關鍵（三）從數據來提升 ROI 的策略

定位：報表

來源基礎：講義拆分

原始網址：https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

母表保留的原來源摘錄：

> 產出什麼報表
