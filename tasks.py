import json

FILE = "data/tasks.json"


def load_tasks():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = input("Enter task: ")

    tasks = load_tasks()

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:\n")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def complete_task():
    tasks = load_tasks()

    view_tasks()

    try:
        task_no = int(input("Enter task number: "))

        tasks[task_no - 1]["completed"] = True

        save_tasks(tasks)

        print("Task completed!")

    except:
        print("Invalid task number")


def delete_task():
    tasks = load_tasks()

    view_tasks()

    try:
        task_no = int(input("Enter task number: "))

        tasks.pop(task_no - 1)

        save_tasks(tasks)

        print("Task deleted!")

    except:
        print("Invalid task number")