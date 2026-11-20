import csv
from pathlib import Path
import piechart

filename = "expenses.csv"
file_exists = Path(filename).exists()

with open(filename, "a", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    
    if not file_exists:
        writer.writerow(["date", "amount", "category"])

    print("請輸入消費紀錄（格式：日期 金額 類別，例如 2026-11-17 100 Transport）")
    print("輸入完畢請直接按 Enter 結束：")


    date, price ,category = input().split()
    price = int(price)

    writer.writerow([date, price, category])

piechart.main()