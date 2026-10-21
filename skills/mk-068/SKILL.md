---
name: mk-068
description: "行銷費用配置上限。用於電商淨利目標下的財務模型、可用行銷預算與利潤再投入比例決策，包含含稅售價、逐單及公司費用、競品價帶、再投入分母和期間；交可重算模型及條件式預算。純損平ROAS或既有Meta活動加碼依該需求處理"
---

# MK-068｜行銷費用配置上限

一般對話請上傳 `packs/mk-068.md`，其中已包含共用規則、本文及必要參考

## 工作目的

這個技能交付：**成本限制下的可用預算表**

資源反推不等於預測或最佳配置；沒有可承擔上限時不自行決定真實支出

## 必要資料

先依本題要完成的工作取用資料，已有值可直接代入或推算

- 費用上限：同期間、同口徑的行銷前可用貢獻、尚未扣除的固定費與核准目標利潤；若可用貢獻未知，再取營收與對應成本推算
- 訂單與流量反推：在收入目標已知或可推算後，取客單與轉換率；已直接提供訂單或流量需求時，沿用其口徑與來源
- 淨利模型：取收入、逐單與公司費用、目標淨利定義及適用稅額假設，按下方 A–C 節補足會改變結果的欄位
- 利潤再投入：另取利潤基礎、比例的分母與期間、既有預算、收付時點及可承擔額度，依 D–E 節比較候選

只問公式或方法時，先交公式與明示假設範例；實際試算才追問該分支缺少的數值

## 方法步驟

1. 確認本題要算費用上限、反推訂單與流量，或評估淨利／再投入；固定期間、成本口徑及目標
2. 純費用上限直接代入下方公式，核對是否重扣費用與結果是否可行；需要訂單或流量需求時，再依客單與轉換率反推
3. 淨利建模依 A–C 節，利潤再投入再接 D–E 節，交付與本題對應的結果；配置預算時以目標及可承擔上限判斷，不把降低單位取得成本等同砍預算

## 計算與判讀

可用行銷費用＝可用貢獻－本期需承擔固定費－核准目標利潤；依本案既定財務口徑計算，已含行銷費的貢獻先拆回行銷前口徑，避免重扣

以下補充在淨利模型或利潤再投入問題時適用；純既定口徑的上限計算直接代入，七個原交付欄位保留

### A. 固定問題與試算口徑

保留全部價格、幣別、稅率假設、成本、目標淨利率、競品自述、供應商報價及補充問句。先辨別問題要建模方法、條件式建議，或要替實際店家決定精確售價與預算；方法問題直接交公式、已知數字試算及可填表格

每個輸入記來源、期間、每件/每單/每月、含稅或未稅、假設或實績。折扣與退款用淨收入時不重扣；買家付運費與物流支出分開。代收銷售稅從收入剔除，進項稅是否可抵扣依實際身分與交易確認，未知時保留分支，不自選國別稅制

平台月費、按單費、百分比費及廣告獲客成本的分母各自確認。固定費除以訂單數是分攤假設，不能把全月費重複放進每件，再在公司層重扣。廣告費只在模型一處列支，明確區分媒體費與總行銷費

### B. 接成完整損益

以商品/訂單組合及月份建表：

| 變數 | 定義 |
|---|---|
| R | 同期間未稅淨收入，按實際組合加總數量×淨價 |
| V | 非廣告變動費，商品、包裝、履約、金流、通路、退貨等按各自驅動因素加總 |
| A | 本期行銷費，媒體、素材及其他適用項目拆開後加總 |
| F | 尚未在其他欄計入的本期固定/階梯費 |
| D、I、T | 未重複計入的折舊、利息及所得稅 |
| N | 稅後淨利＝R−V−A−F−D−I−T |

若任務的淨利定義不同，保留其定義並明列差異。缺所得稅或公司費用時，交已列費用差額及待填欄，不能稱完整稅後淨利。R>0才計N/R；零收入時交金額與費用，不用零比率遮蔽問題

目標淨利率m是約束N≥mR。已確認同口徑且各其他費用及T暫固定時，行銷上限為 R−V−F−D−I−T−mR；負上限代表這組收入/成本連不投廣告也達不到目標，不能把上限歸零後說可達標。所得稅隨利潤或費用抵扣變動時，按已確認稅額規則聯動重算，保留目標是否可行

售價反推只在明列假設成立時使用。例如單件非比例成本c、所有其他成本已攤入且不隨價格改變、目標率m<1，所需未稅價c/(1−m)。另有收入比例費k時為c/(1−m−k)，分母須正；混合含稅計費須回到原費用基準，不能全視為未稅收入比例。反推價格是成本邊界，不能當願付價或未來銷量證據

### C. 與市場、供應和銷量一起比較

用同規格、同數量、相同配送與稅口徑比較報價；首家報價不等於整體市場成本。將使用者競品價帶保留，超出價帶的反推價格列為待驗證的價值/願付假設，不直接命令漲價

比較使用者能採取的價格、供應商、包裝、物流、組合及廣告效率情境，各組包含完整收入和成本。調價會影響銷量與按價格計費；加廣告不假定效率不變。沒有歷史就明示假設，不任意賦予機率或稱最佳方案

量大降單價同時檢查MOQ、品質、整批付款、庫存及履約限制。採購未售庫存、借款本金及資本支出與本期損益分開記，並接到現金表。實際前後比較用同口徑成熟資料更新原假設，保留預估版本

### D. 把再投入比例還原成金額

對每個百分比保留分子、分母、期間、已扣費用及包含既有預算與否。競品自述比例不能直接當決策標準

- 本期行銷費/本期淨收入：這是收入占比，不能叫利潤再投入率
- 上期已實現利潤P，撥比例q給下期：候選金額qP。先明定是下期總預算或增額；增額情況加上既有預算A0。上期撥款不改變上期已實現利潤，行銷費在下期實際發生時才列下期損益，撥款也不是下期新收入
- 本期總行銷費A等於本期扣完A後利潤的q：設其他成本及所得稅金額固定、扣A前餘額B，則A=q(B−A)，解為qB/(1+q)。這跟qB不同；稅額、收入或成本隨A變動時重新聯立情境，不能套簡式

P≤0時沒有正的利潤撥款基礎。仍要投入須明列啟動資金或其他資金來源及可承受損失，不能虛構正利潤。分母為零時比率未定義，仍能比較有來源的預算金額

### E. 選擇再投入金額

針對候選金額逐一核對三項：

1. 損益：以新預算及其銷量/效率情境重算，保留目標淨利或明確的成長期虧損計畫；不能私自把10–25%目標改成先虧損
2. 現金：依付款時點列期初可用資金、收款、供應商、稅款、薪資、備貨、借款本金、資本支出與預算。每期結餘須滿足使用者的保留額；同一支出只計一次。正淨利不等於有現金，尚未實現的預期利潤不算現有資金
3. 新增效益：預期新增訂單貢獻減新增行銷與階梯費後是否支持該方案。全部自然成交、平台歸因和過去平均ROAS都不能直接證明新增貢獻；無證據時交有期限、支出及損失上限、成果口徑與停止條件的測試候選

選擇同時符合條件且有依據的金額，再除以已明定的正利潤基礎形成比例。不強制花滿上限；無可行候選時交不再投入、調整成本/定價或待補資料。需要保留額、實際支出上限或精確金額而未提供時，用待填參數交條件式決策，不自創固定35%、70%、20%增幅或觀察天數

### F. 交付與完成核對

交一份整合成果：原始數字重算、可複製的月損益與現金欄位/公式、目標情境表、市場及成本差距、各百分比正確定義、候選預算選擇與更新/停止條件。數字標示原始值、推導、假設或未知，每項原問句均有對應成果

方法問題可用完整模型與條件式示範完成；若原題要求店家的實際金額、經驗或實測，必須取得相應資料及結果。Skill 可執行、方法驗收通過與原題實際解決分開記錄

### G. 來源與採用範圍

以 [行銷策略實戰學程Day2](https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit) 第3、7、25、27、38–49頁的利潤回推、成本及損平方法為主體，2026-10-08全文讀取104頁，revision AacEra95twlfAw。按個案實際成本建模，不套用課堂健康比例、固定費三倍或達損平即可放心加碼

MIT 補充採 [financial-analyst](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/finance/skills/financial-analyst/SKILL.md) 及 [forecasting-best-practices](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/finance/skills/financial-analyst/references/forecasting-best-practices.md) 的驅動模型、情境、收付時間與實績更新，不採上游固定機率、誤差目標或SaaS門檻。再投入分母、跨期與代數分支是依本方法交付要求整合的規則

官方交叉核對：[business.gov.au 預算建立](https://business.gov.au/finance/financial-tools-and-templates/create-a-budget) 支持預算、預測及實績區分；[現金管理](https://business.gov.au/guide/guide-to-managing-cash-flow) 支持付款、庫存與更新的現金檢查

#### MIT 授權

MIT License

Copyright (c) 2025 Alireza Rezvani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 固定交付欄位

| 順序 | 欄位 | 填寫方式 |
|---:|---|---|
| 1 | 輸入變數 | 原始證據、方法中間結果或明確未知；不得補造 |
| 2 | 數值 | 原始證據、方法中間結果或明確未知；不得補造 |
| 3 | 單位與口徑 | 原始證據、方法中間結果或明確未知；不得補造 |
| 4 | 來源 | 原始證據、方法中間結果或明確未知；不得補造 |
| 5 | 計算式 | 原始證據、方法中間結果或明確未知；不得補造 |
| 6 | 結果 | 原始證據、方法中間結果或明確未知；不得補造 |
| 7 | 限制 | 原始證據、方法中間結果或明確未知；不得補造 |

## 核對案例

**MK-068-C05｜必要分母為零**

預期：回報公式不成立，不輸出零成本或無限目標

**MK-068-C06｜只提供部分成本**

預期：保留局部結果與未納入項目，不稱完整獲利

## 方法來源

原始檔：行銷策略實戰學程Day2-以終為始x降低成本x提升指標

定位：成本

來源基礎：講義拆分

原始網址：https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

母表保留的原來源摘錄：

> 以終為始 x 降低成本 x 提升指標
