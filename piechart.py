
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


def load_expenses(filename="expenses.csv"):
    totals = defaultdict(float)

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["category"].strip()
            amount = float(row["amount"])

            if category and amount > 0:
                totals[category] += amount

    return dict(totals)


def main():
    filename = "expenses.csv"

    if not Path(filename).exists():
        print("Error: expenses.csv not found.")
        return

    try:
        totals = load_expenses(filename)
    except (ValueError, KeyError) as error:
        print("Invalid expense data:", error)
        return

    if not totals:
        print("No expenses to display.")
        return

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(8, 6))
    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expenses by Category")
    plt.axis("equal")
    plt.tight_layout()

    plt.savefig("expense_piechart.png", dpi=300)
    print("Pie chart saved as expense_piechart.png")

    plt.show()


if __name__ == "__main__":
    main()
