import json

FILE = "data/expenses.json"


def load_expenses():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_expenses(expenses):
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    category = input("Enter Category :")
    amount = float(input("Enter Amount : "))

    data = load_expenses()
    data.append({"category": category, "amount": amount})

    save_expenses(data)

    print("Expenses Added sucessfully!")


def view_expenses():
    data = load_expenses()

    if not data:
        print("No expenses found")

    else:
        for i, expense in enumerate(data):
            print(f"{i+1}. {expense['category']:<12} ₹{expense['amount']:.2f}")


def total_expenses():
    data = load_expenses()

    total_amount = 0
    for expense in data:
        total_amount += expense["amount"]

    print(f"Total Expenses: ₹{total_amount:.2f}")


def delete_expense():
    data = load_expenses()

    if not data:
        print("No expenses found")
        return

    else:
        for i, expense in enumerate(data):
            print(f"{i+1}. {expense['category']:<12} ₹{expense['amount']:.2f}")

    try:
        item_no = int(input("Enter the expense number for deletion :"))
        data.pop(item_no - 1)
        print("Expense deleted successfully!")

    except (ValueError, IndexError):
        print("Invalid Expense Number!")

    save_expenses(data)


def search_expenses():
    data = load_expenses()

    if not data:
        print("No expenses found")
        return

    print("Search expenses by category")

    category_name = input("Enter the category : ")

    found = False

    for expense in data:
        if expense["category"].lower() == category_name.lower():
            print(f"{expense['category']:<12} ₹{expense['amount']:.2f}")
            found = True

    if not found:
        print("No expenses found for this category.")
