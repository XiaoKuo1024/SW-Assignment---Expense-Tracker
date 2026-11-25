import csv
from pathlib import Path
import piechart

filename = "expenses.csv"
file_exists = Path(filename).exists()

with open(filename, "a", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    
    if not file_exists:
        writer.writerow(["date", "amount", "category"])

    print("輸入完畢按兩次 Enter 結束：")
    print("[YYYY-MM-DD, price, category]")

    while True:
        try:
            line = input().strip()

            if not line:
                break

            date, price ,category = line.split()
            price = int(price)

            writer.writerow([date, price, category])

        except ValueError:
            print("輸入格式錯誤")
            break
        except EOFError:
            break

piechart.main()