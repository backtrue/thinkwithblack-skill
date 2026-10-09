---
name: mk-261
description: "商品條碼完整性檢查。用於需要GTIN 等識別欄位的缺漏的工作；依本項方法處理已指定資料並核對交付"
---

# MK-261｜商品條碼完整性檢查

一般對話請上傳 `packs/mk-261.md`，其中已包含共用規則、本文及必要參考

## 工作目的

這個技能交付：**GTIN 等識別欄位的缺漏**

保留原任務名稱與交付範圍；方法編撰性質：依母表任務與已核准入口要求編撰；不是宣稱逐字源自講義的新增規則；原來源為課程大綱，細部方法仍需核准／覆核。不得從這份草稿推導出未授權的產品行為、商業門檻或平台能力

ID無法一對一匹配時保留未匹配，不猜對應；沒有完整事件樣本不捏造匹配率

## 必要資料

請提供：商品 Feed、網站實際資訊、SKU 成效及拒登訊息

## 方法步驟

1. 從 Merchant Center／Product Feed 與實際商品資料開始，只處理「商品條碼完整性檢查」
2. 大綱明確支持 Title、Description、Image、Price、Availability、Brand、GTIN、Google Product Category、Product Type、Custom Label、Product Group、Shopping Search Terms 與拒登／資料品質診斷
3. 產出「GTIN 等識別欄位的缺漏」時必須回指實際 Feed、SKU 成效、搜尋字詞或拒登訊息；缺資料時只列缺件
4. Merchant Center 欄位要求、拒登規則與 Shopping 現行功能會變動，正式執行前另查 Google 官方現況；大綱未提供的固定規則不補造

## 計算與判讀

商品規格與價格以商品資料為準；目錄欄位及拒登規則在製作時驗證

## 固定交付欄位

| 順序 | 欄位 | 填寫方式 |
|---:|---|---|
| 1 | 對象／位置 | 原始證據、方法中間結果或明確未知；不得補造 |
| 2 | 採用條件 | 原始證據、方法中間結果或明確未知；不得補造 |
| 3 | 實際證據 | 原始證據、方法中間結果或明確未知；不得補造 |
| 4 | 檢查狀態 | 原始證據、方法中間結果或明確未知；不得補造 |
| 5 | 差異／原因候選 | 原始證據、方法中間結果或明確未知；不得補造 |
| 6 | 下一工作 | 原始證據、方法中間結果或明確未知；不得補造 |
| 7 | 限制 | 原始證據、方法中間結果或明確未知；不得補造 |

## 核對案例

**MK-261-C05｜資料显示符合現有條件**

預期：回報可用或維持，不製造修改需求

**MK-261-C06｜工具回傳錯誤**

預期：回報未取得，不能把它列成業務異常

## 方法來源

原始檔：AI × Google Ads 搜尋廣告實戰課｜五堂課程大綱

定位：GTIN

來源基礎：大綱延伸

原始網址：https://docs.google.com/document/d/10HOKMeR1qM9_LXmc7pYGXJ6tbOMJtBuFAxcuCCAJZk4/edit

母表保留的原來源摘錄：

> • Product Feed 的核心欄位：Title、Description、Image、Price、Availability、Brand、GTIN、Google Product Category、Product Type、Custom Label 等

### 補充來源定位

原教材的來源核對紀錄

- 來源代碼：GO
- 原始定位：GTIN
- 原始大綱證據：• Product Feed 的核心欄位：Title、Description、Image、Price、Availability、Brand、GTIN、Google Product Category、Product Type、Custom Label 等
