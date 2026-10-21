---
name: mk-262
description: "商品自訂標籤設計。用於需要毛利、價位、活動與產品線標籤的工作；依本項方法處理已指定資料並核對交付"
---

# MK-262｜商品自訂標籤設計

一般對話請上傳 `packs/mk-262.md`，其中已包含共用規則、本文及必要參考

## 工作目的

這個技能交付：**毛利、價位、活動與產品線標籤**

執行步驟由 ThinkWithBlack 依本方法的工作目的整理，2026-10-21；課程大綱與原始來源保留於文末

ID無法一對一匹配時保留未匹配，不猜對應；沒有完整事件樣本不捏造匹配率

## 必要資料

SKU、成本與毛利定義、價格、活動及產品線、既有標籤與本案區間規則

## 方法步驟

1. 先列每一標籤要支援的管理決策，分開毛利、價位、活動與產品線維度
2. 為每個維度定義名稱、允許值、數值區間含界線、資料來源及更新時點；沒有品牌切點時列待定
3. 逐 SKU 套規則，缺值與多重命中另列；交付標籤字典及商品對照，確認當前 Merchant Center 自訂標籤規格後再轉成匯入欄位

## 計算與判讀

毛利與價格先固定幣別及成本口徑；區間需無重疊且明確處理未分類商品

## 固定交付欄位

| 順序 | 欄位 | 填寫方式 |
|---:|---|---|
| 1 | 維度與用途 | 填入已提供來源、計算或明確未知 |
| 2 | 欄位及允許值 | 填入已提供來源、計算或明確未知 |
| 3 | 區間與來源 | 填入已提供來源、計算或明確未知 |
| 4 | SKU 對照 | 填入已提供來源、計算或明確未知 |
| 5 | 缺值或衝突 | 填入已提供來源、計算或明確未知 |
| 6 | 更新時點 | 填入已提供來源、計算或明確未知 |

## 核對案例

**MK-262-A1｜價格 100 同時命中「≤100」與「≥100」**

預期：修正界線後才指派

**MK-262-A2｜成本未知**

預期：毛利標籤待定，不以售價假裝毛利

## 方法來源

原始檔：AI × Google Ads 搜尋廣告實戰課｜五堂課程大綱

定位：Custom Label

來源基礎：大綱延伸

原始網址：https://docs.google.com/document/d/10HOKMeR1qM9_LXmc7pYGXJ6tbOMJtBuFAxcuCCAJZk4/edit

母表保留的原來源摘錄：

> • Product Feed 的核心欄位：Title、Description、Image、Price、Availability、Brand、GTIN、Google Product Category、Product Type、Custom Label 等

### 補充來源定位

原教材的來源核對紀錄

- 來源代碼：GO
- 原始定位：Custom Label
- 原始大綱證據：• Product Feed 的核心欄位：Title、Description、Image、Price、Availability、Brand、GTIN、Google Product Category、Product Type、Custom Label 等
