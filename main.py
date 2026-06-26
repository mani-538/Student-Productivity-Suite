from tasks import *
from attendance import *
from cgpa import *
from expenses import *

while True:
    print("\n===== Student Productivity Suite =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")

    print("5. Add Attendance")
    print("6. View Attendance")
    print("7. Update Attendance")

    print("8. Calculate CGPA")

    print("9. Add Expense")
    print("10. View Expenses")
    print("11. Total Expenses")
    print("12. Delete Expense")
    print("13. Search Expense")

    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        add_attendance()

    elif choice == "6":
        view_attendance()

    elif choice == "7":
        update_attendance()

    elif choice == "8":
        cgpa = calculate_cgpa()
        print(f"Your CGPA is {cgpa:.2f}")

    elif choice == "9":
        add_expense()

    elif choice == "10":
        view_expenses()

    elif choice == "11":
        total_expenses()

    elif choice == "12":
        delete_expense()

    elif choice == "13":
        search_expenses()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
