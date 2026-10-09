# 教材版本與維護

## 取得與更新

版本寫在 INDEX.md 與 catalog.json。從 Skills 儲存庫或 Google Drive 取得同版本教材後，使用新索引及方法包；舊對話需要新方法時上傳新版檔案

## 維護命令

需要 Python 3.10 或更新版本，使用標準函式庫

```sh
python3 scripts/build-free-edition.py generate
python3 scripts/verify-public-skills.py
python3 -m unittest discover -s tests
python3 scripts/build-free-edition.py package --output /absolute/output/directory
```

free-content.json 是公開清單；方法本文、必要參考與 PUBLIC_SKILL_RULES.md 是內容來源。生成工具更新索引、單檔方法包與 catalog.json；檢查工具核對檔案、引用與生成結果

package 先驗證，再產生教材 ZIP、乾淨來源 ZIP 與逐檔雜湊紀錄。將同一個教材 ZIP 提供給儲存庫下載入口與 Google Drive，核對 ZIP 雜湊與版本

公開前檢查將開放的 Git 歷史、既有附件及下載檔是否符合相同範圍。乾淨來源 ZIP 可用來建立新的公開歷史
