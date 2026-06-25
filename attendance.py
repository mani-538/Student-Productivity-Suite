import json

FILE = "data/attendance.json"

def load_attendance():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except:
        return {}

def save_attendance(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_attendance():
    subject = input("Enter subject: ")

    attended = int(input("Classes attended: "))
    total = int(input("Total classes: "))

    data = load_attendance()

    data[subject] = {
        "attended": attended,
        "total": total
    }

    save_attendance(data)

    print("Attendance added successfully!")

def view_attendance():
    data = load_attendance()

    if not data:
        print("No attendance records found.")
        return

    print("\nAttendance Report\n")

    for subject, details in data.items():

        attended = details["attended"]
        total = details["total"]

        percentage = (attended / total) * 100

        print(
            f"{subject}: {attended}/{total} "
            f"({percentage:.2f}%)"
        )

def update_attendance():

    data = load_attendance()

    subject = input("Enter subject name: ")

    if subject not in data:
        print("Subject not found.")
        return

    attended = int(input("New attended classes: "))
    total = int(input("New total classes: "))

    data[subject]["attended"] = attended
    data[subject]["total"] = total

    save_attendance(data)

    print("Attendance updated.")