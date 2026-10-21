---
name: mk-261
description: "商品條碼完整性檢查。用於需要GTIN 等識別欄位的缺漏的工作；依本項方法處理已指定資料並核對交付"
---

# MK-261｜商品條碼完整性檢查

一般對話請上傳 `packs/mk-261.md`，其中已包含共用規則、本文及必要參考

## 工作目的

這個技能交付：**GTIN 等識別欄位的缺漏**

執行步驟由 ThinkWithBlack 依本方法的工作目的整理，2026-10-21；課程大綱與原始來源保留於文末

ID無法一對一匹配時保留未匹配，不猜對應；沒有完整事件樣本不捏造匹配率

## 必要資料

Feed 商品識別欄、製造商或包裝原始資料、商品變體、目前 Merchant Center 診斷

## 方法步驟

1. 以商品與變體鍵逐筆對照原始識別資料，保留無法匹配項
2. 區分缺值、格式問題、與原始條碼不一致，以及原本沒有製造商識別碼；缺條碼不猜造
3. 對每個問題列原值、應採來源與修正建議；依本商品類型查 Google 當前識別欄要求，修正後再讀回診斷

## 計算與判讀

網站同品名不等於同變體；沒有診斷讀回時交待核對項，不標已恢復刊登

## 固定交付欄位

| 順序 | 欄位 | 填寫方式 |
|---:|---|---|
| 1 | 商品與變體鍵 | 填入已提供來源、計算或明確未知 |
| 2 | Feed 原值 | 填入已提供來源、計算或明確未知 |
| 3 | 製造商證據 | 填入已提供來源、計算或明確未知 |
| 4 | 缺漏或衝突 | 填入已提供來源、計算或明確未知 |
| 5 | 建議值與依據 | 填入已提供來源、計算或明確未知 |
| 6 | 適用規則來源 | 填入已提供來源、計算或明確未知 |
| 7 | 讀回狀態 | 填入已提供來源、計算或明確未知 |

## 核對案例

**MK-261-A1｜同商品兩尺寸各有不同條碼**

預期：逐變體匹配

**MK-261-A2｜製造商未提供條碼**

預期：列缺資料與適用規則，不產生隨機 GTIN

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
