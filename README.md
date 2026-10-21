[English — all 365 skills](en/README.md) · 繁體中文

<div align="center">

# Marketing Skills for Everyone

**by ThinkWithBlack**

## 365 個免費 AI 行銷 Skills

**一天一個 Skill，解決一個行銷問題**

由 [邱煜庭（小黑老師）](#認識整理這套方法的小黑老師) 整理，把行銷方法帶進你的 AI 對話

商品賣點、廣告文案、活動預算、單品毛利、顧客回購<br>從你今天卡住的那一題開始

[![365 Skills](https://img.shields.io/badge/行銷_Skills-365-171717?style=flat-square)](INDEX.md) [![Markdown](https://img.shields.io/badge/使用方式-上傳_Markdown-F2C94C?style=flat-square&labelColor=171717)](START_HERE.md) [![MIT License](https://img.shields.io/badge/License-MIT-171717?style=flat-square)](LICENSE)

**[下載完整教材包 ↓](https://github.com/backtrue/thinkwithblack-skill/releases/latest)** · **[逛逛 365 個 Skills](INDEX.md)** · **[開始第一題](#三步開始你的第一題)**

覺得這份工具箱值得留著，點右上角 **Star ⭐** 收藏，下次遇到行銷問題再回來

</div>

---

> **更新資訊｜2026-10-21**：現在也能用 `npx ai-marketing-skills` 選擇方法，安裝到 Claude Code、Codex 或 Cursor，或匯出給一般 AI 對話使用。安裝環境與完整指令見 [npm 套件說明](https://www.npmjs.com/package/ai-marketing-skills)

## 把今天的工作，交給有方法的 AI

「這個商品到底有什麼賣點？」「廣告費加下去，每賣一盒還剩多少？」「客人買過一次，下一次要怎麼找他回來？」

**Marketing Skills for Everyone** 是 ThinkWithBlack 整理的 **365 份可上傳行銷方法包**。每份都帶著需要的資料、處理步驟、交付格式與核對方式，讓 AI 有方法可循，也讓你有依據檢查成果

**說出你的問題，讓 AI 從索引選方法。** 你再上傳它需要的那一份，就能開始一起做，不必先記住 365 個名稱

## 我為什麼把這套 Skills 開源

從「網路行銷零元本舖」開始，我一直希望縮小資訊落差，幫助每一家企業建立自己的行銷能力。過去我透過教學做這件事，到了 AI 時代，我想把十幾年的實戰教學，以及持續至今的第一線工作經驗，整理成能和 AI 一起使用的方法

但整理 Skills 的過程中，我一直在想：如果一個人沒有預算訂閱 AI，他拿到這些方法以後，真的用得起來嗎？知識開放了，使用知識的工具卻可能又成為一道門檻

我也很在意另一件事：如果你原本就不熟悉行銷，怎麼知道 AI 講得對不對？看起來完整的答案，可能藏著錯誤。我希望這套 Skills 能把需要的資料、判斷步驟與核對方式一起交給你，讓你練習處理問題，也有依據檢查結果

這就是 Marketing Skills for Everyone 裡 Everyone 的意思。我希望沒有訂閱預算的人，也能從免費的方法包與操作教學開始，把自己的商品、成本或文案帶進來，一步一步練習

「遇事能決」是我把這套 Skills 開源的核心目的：遇到問題時，知道怎麼判斷、下一步該怎麼做，逐步建立自己的行銷能力

免費版提供可以實際使用的行銷方法；付費 MCP 提供資料串接與自動化，企業導入則處理客製開發、導入陪跑與持續維護。我希望大家先有機會把方法用起來，再依自己的工作需要選擇服務

[閱讀我談 AI、學習機會與資源差距的原文](https://www.facebook.com/backtrue/posts/pfbid0194Rrzy4dXVWXjKxFmnr9eLppVzJiEU8hqDXtBvWDTBCBhu4tB5fQgdEu7yVNR8xl)

## 認識整理這套方法的小黑老師

<a href="https://bio.thinkwithblack.com/"><img src="https://thinkwithblack.com/learning-media/chiu-yu-ting.jpg" alt="邱煜庭（小黑老師）" width="180" height="270"></a>

**邱煜庭（小黑老師）｜Marketing Skills for Everyone 整理者**

長年從事行銷策略、數位廣告、電商經營與教學，現為燒賣研究所首席顧問，曾任 uitox 全球電子商務集團行銷總監、百腦匯（中國）總部行銷經理。工作與授課經歷見[燒賣研究所講師介紹](https://www.shumai.com.tw/backtrue)

從 2004 年開始投入 SEO，持續教授搜尋、行銷與 AI 工作應用，並著有《網路集客力：從 SEO 到 Facebook 的行銷新方略》。[SEO 與教學背景](https://aeogeo.thinkwithblack.com/about) · [著作與出版資料](https://www.eslite.com/product/1001122231993940)

**[認識小黑老師的完整經歷與課程 →](https://bio.thinkwithblack.com/)**

## 先看一題：一盒餅乾，賣完剩多少？

用教材附的[餅乾成本練習](examples/cookie-costs.md)，搭配[單品貢獻毛利計算](packs/mk-059.md)，可以練習把零散成本整理成一筆能核對的計算

> 幫我算每賣出一盒餅乾，扣掉這些成本後，還剩多少貢獻？請列出公式和每一筆成本

| 這題提供的資料 | 每盒金額 |
|---|---:|
| 商品淨收入，已扣稅、折扣與退款 | NT$600 |
| 食材＋包裝＋每盒增加的製作人力 | NT$150＋50＋80 |
| 店家物流＋平台與金流費＋分攤廣告費 | NT$60＋30＋40 |

**算完得到：每盒貢獻 NT$190**

```text
600 −（150 ＋ 50 ＋ 80 ＋ 60 ＋ 30 ＋ 40）＝ 190
```

這是教材中的虛構練習：買家運費收入為 0，已確認沒有其他變動成本；固定薪資與租金另外計算

接著你可以換一題：「那些只買過一次的客人，第二次該推薦什麼？」AI 依同一份索引選擇[第一次回購促進計畫](packs/mk-390.md)，請你補上新的方法包與顧客資料，繼續處理下一件工作

## 今天先解決哪一題？

| 你手上的問題 | 打開這個 Skill | 要完成的東西 |
|---|---|---|
| 商品特色很多，哪些真的能拿來寫文案？ | [商品事實整理](packs/mk-001.md) | 可引用的商品事實表、還缺哪些證據 |
| 售價扣完成本，這筆生意剩多少？ | [單品貢獻毛利計算](packs/mk-059.md) | 每筆成本、計算公式與單品貢獻 |
| 檔期廣告預算怎麼抓？ | [檔期預算與獲利預估](packs/forecast-event-profit.md) | 依歷史資料估算的預算、營收與貢獻情境 |
| 只買過一次的客人，接下來怎麼聯繫？ | [第一次回購促進計畫](packs/mk-390.md) | 回購時點、第二件商品與提醒安排 |
| 電子報內容有了，主旨怎麼寫？ | [電子報主旨草稿](packs/mk-411.md) | 對應信件內容的主旨草稿 |
| 會員規則連同事都說不清楚？ | [會員規則簡化與理解檢查](packs/simplify-member-rules.md) | 顧客版說明、改寫對照與理解測試題 |

**[查看完整 365 個 Skills →](INDEX.md)**

## 三步開始你的第一題

### 1. 下載教材，上傳索引

[下載完整教材包](https://github.com/backtrue/thinkwithblack-skill/releases/latest)並解壓縮，在 ChatGPT、Claude、Gemini 等支援檔案閱讀的 AI 對話中，上傳 `INDEX.md`

### 2. 貼上這段指示，加上你的問題

```text
請先讀取附件 INDEX.md，從索引選出適合我這次問題的方法
如果你還沒讀到方法全文，請告訴我要上傳哪個 packs/*.md，等我上傳後再開始
後續換題時，請重新查索引；需要其他方法包，就告訴我檔名

我的問題是：【填入你現在要處理的工作】
```

### 3. 上傳方法包與資料，開始做

依 AI 指定的檔名，從 `packs/` 上傳對應的 `.md`，再附上本題的商品資料、報表或草稿。每份方法包都已合併完整步驟、共用規則、必要參考與授權

還沒準備好自己的資料，可以先用[虛構練習資料](examples/README.md)跑第一題；經常處理同一個品牌，可以填一份[品牌背景表](context/MARKETING_CONTEXT.template.md)一起上傳

**方法全文用上傳的，只需貼一次上面的起手指示。** 詳細操作見 [START_HERE.md](START_HERE.md)

## 下載後，你會拿到什麼？

| 檔案 | 拿來做什麼 |
|---|---|
| [`INDEX.md`](INDEX.md) | 讓 AI 查方法、選出這次需要的 Skill |
| `packs/` | 365 份完整方法包，選到哪份就上傳哪份 |
| [`examples/`](examples/README.md) | 商品事實、成本、回購與會員規則的虛構練習資料 |
| [`context/`](context/MARKETING_CONTEXT.template.md) | 可自行填寫的品牌背景表 |
| [`START_HERE.md`](START_HERE.md) | 第一次使用、追問換題與附件讀取的操作說明 |

免費版就是 **thinkwithblack-skill 與 Google Drive 共用的這套內容**，包含方法、必要參考與範例。習慣用雲端資料夾，也可以從 [Google Drive 下載](https://drive.google.com/drive/folders/1X9bg6MbHY7dkzj0xOqbYrM10Ia6AKkCp)

<details>
<summary><strong>同一段對話換題，要重新開始嗎？</strong></summary>

直接提出新的問題，AI 會依起手指示重新查索引；缺哪份方法全文，再上傳哪一份。同一題改稿或補資料，接著說明即可

開啟新的對話時，重新上傳索引與該題的方法包

</details>

<details>
<summary><strong>可以直接貼 Google Drive 連結嗎？</strong></summary>

可以提供單一檔案的可讀連結，讓 AI 確認讀到方法全文。若對話讀不到連結，就下載同一份 `.md` 再上傳；只貼資料夾連結，不會把裡面所有方法載入對話

</details>

<details>
<summary><strong>想看方法來源，或協助修改內容？</strong></summary>

方法來源與第三方授權保留在各方法包中，歡迎依 [CONTRIBUTING.md](CONTRIBUTING.md) 提供修訂

公開範圍由 [free-content.json](free-content.json) 管理；版本與更新方式見 [RELEASE.md](RELEASE.md)，調整紀錄見 [CHANGELOG.md](CHANGELOG.md)

</details>

## 把方法接進日常工作

需要連接帳戶資料、安排多個方法接續工作、持續追蹤或實際操作時，由 **ThinkWithBlack MCP** 承接進階服務。完整分工見[免費內容與進階服務](PUBLIC_BOUNDARY.md)

## 覺得有幫助，留一顆 Star

**在頁面右上角點一下 Star ⭐，把這 365 個方法收進你的 GitHub 收藏**

也歡迎把這個專案分享給那位每天都在想文案、算預算、研究客人為什麼不回購的同事。找到適合自己的第一個 Skill，就從那一題開始

**[下載教材，開始第一題 ↓](https://github.com/backtrue/thinkwithblack-skill/releases/latest)**

## 特別感謝

感謝 [wang.joan.888](https://www.facebook.com/wang.joan.888) 與 [leo.chang.96387189](https://www.facebook.com/leo.chang.96387189) 協助優化 Marketing Skills for Everyone，讓這套方法更好用

## 授權

本專案採 [MIT 授權](LICENSE)，引用來源與第三方授權隨各方法保留
