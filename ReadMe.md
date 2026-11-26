# Expense Tracker（記帳與支出分析工具）

這是一個以 Python 開發的命令列記帳與支出視覺化工具，支援多筆消費紀錄輸入、輸入格式防呆檢查、總支出與分類佔比統計，並自動產生支出分布圓餅圖（`expense_piechart.png`）。

---

## 📁 專案結構

```text
SW-Assignment---Expense-Tracker/
├── main.py                # 主程式與使用者輸入／防呆驗證模組
├── piechart.py            # 資料統計與圓餅圖繪製模組
├── expenses.csv           # 消費紀錄資料檔（程式執行時自動寫入／更新）
├── expense_piechart.png   # 輸出的支出圓餅圖範例圖檔
└── README.md              # 專案說明文件