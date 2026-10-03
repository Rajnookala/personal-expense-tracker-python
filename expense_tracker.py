import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file with headers if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])


def add_expense():
    """Add a new expense to the CSV file."""
    print("\n--- Add Expense ---")

    date = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    category = input("Category (Food/Travel/Shopping/Bills/Other): ").strip().title()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount: ").strip())
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive amount.")
        return

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, f"{amount:.2f}", description])

    print("Expense added successfully!")


def get_expenses():
    """Read all expenses from the CSV file."""
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def view_expenses():
    """Display all recorded expenses."""
    expenses = get_expenses()

    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'Date':<12} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 65)

    for expense in expenses:
        print(
            f"{expense['date']:<12} "
            f"{expense['category']:<15} "
            f"₹{float(expense['amount']):>9.2f}  "
            f"{expense['description']}"
        )


def total_expenses():
    """Calculate and display total spending."""
    expenses = get_expenses()
    total = sum(float(expense["amount"]) for expense in expenses)

    print("\n--- Total Spending ---")
    print(f"Total expenses: ₹{total:.2f}")


def category_summary():
    """Show spending grouped by category."""
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        summary[category] = summary.get(category, 0) + amount

    print("\n--- Category Summary ---")

    for category, amount in sorted(summary.items(), key=lambda item: item[1], reverse=True):
        print(f"{category:<15} ₹{amount:.2f}")


def monthly_summary():
    """Show spending for a selected month."""
    month = input("\nEnter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format. Use YYYY-MM.")
        return

    expenses = get_expenses()
    monthly_expenses = [
        expense for expense in expenses if expense["date"].startswith(month)
    ]

    total = sum(float(expense["amount"]) for expense in monthly_expenses)

    print(f"\n--- Monthly Summary: {month} ---")
    print(f"Number of expenses: {len(monthly_expenses)}")
    print(f"Total spending: ₹{total:.2f}")


def main():
    initialize_file()

    while True:
        print("\n" + "=" * 40)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Category Summary")
        print("5. Monthly Summary")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
