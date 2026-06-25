from tasks import *
from attendance import *

while True:

    print("\n===== Student Productivity Suite =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("6. Add Attendance")
    print("7. View Attendance")
    print("8. Update Attendance")

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
        print("Goodbye!")
        break

    elif choice == "6":
        add_attendance()

    elif choice == "7":
        view_attendance()

    elif choice == "8":
        update_attendance()

    else:
        print("Invalid choice")
