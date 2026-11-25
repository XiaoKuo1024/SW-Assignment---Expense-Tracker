
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


    print("\n========== Expense Summary ==========")

    for category, amount in totals.items():
        percentage = amount / sum(amounts) * 100
        print(f"{category}: {amount:,.0f} ({percentage:.1f}%)")

    print("-------------------------------------")
    print(f"Total Expenses: {sum(amounts):,.0f}")
    print("=====================================\n")


    
    colors = ["#82B5DB", "#F2BD86", "#8CCDB8", "#C7B5E8", "#F29BA8"]

    plt.figure(figsize=(8, 6))
    plt.pie(
        amounts,
        labels=categories,
        colors=colors,
        autopct=lambda pct: f"{pct:.1f}%\n({pct * sum(amounts) / 100:.0f})",
        startangle=90
    )


    total_expenses = sum(amounts)
    plt.title(f"Expenses by Category\nTotal Expenses: {total_expenses:,.0f}")
    plt.axis("equal")
    plt.tight_layout()

    plt.savefig("expense_piechart.png", dpi=300)
    print("Pie chart saved as expense_piechart.png")

    plt.show()


if __name__ == "__main__":
    main()
