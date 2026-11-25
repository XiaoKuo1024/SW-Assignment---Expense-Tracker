
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt



def load_expenses(filename="expenses.csv"):
    totals = defaultdict(float)

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"date", "amount", "category"}
        actual_columns = set(reader.fieldnames or [])
        missing_columns = required_columns - actual_columns

        if missing_columns:
            raise ValueError(
                "Missing CSV columns: " + ", ".join(sorted(missing_columns))
            )

        for line_number, row in enumerate(reader, start=2):
            category = (row.get("category") or "").strip()
            amount_text = (row.get("amount") or "").strip()

            if not category:
                print(f"Warning: Row {line_number} has no category. Skipped.")
                continue

            try:
                amount = float(amount_text)
            except ValueError:
                print(f"Warning: Row {line_number} has invalid amount. Skipped.")
                continue

            if not (0 < amount < float("inf")):
                print(f"Warning: Row {line_number} has invalid amount. Skipped.")
                continue

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

    plt.figure(figsize=(11, 7))
    
    wedges, texts, autotexts = plt.pie(
        amounts,
        labels=categories,
        colors=colors,
        autopct=lambda pct: f"{pct:.1f}%\n({pct * sum(amounts) / 100:.0f})",
        startangle=90
    )

    legend_labels = [
        f"{category}: {amount:,.0f}"
        for category, amount in zip(categories, amounts)
    ]

    plt.legend(
        wedges,
        legend_labels,
        title="Expense Categories",
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        fontsize=10,
        title_fontsize=11,
        frameon=False
    )



    total_expenses = sum(amounts)
    plt.title(f"Expenses by Category\nTotal Expenses: {total_expenses:,.0f}")
    plt.axis("equal")
    plt.subplots_adjust(left=0.05, right=0.72, top=0.88, bottom=0.08)

    plt.savefig("expense_piechart.png", dpi=300)
    print("Pie chart saved as expense_piechart.png")

    plt.show()


if __name__ == "__main__":
    main()
