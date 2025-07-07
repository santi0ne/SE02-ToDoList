tasks = []

def add_task():
    task = input("Enter the task to add: ")
    tasks.append({"task": task, "is_complete": False})
    print("Task added.")

def list_tasks():
    if not tasks:
            print("No tasks found.")
    else:
        for i, t in enumerate(tasks):
            status = "x" if t["is_complete"] else "-"
            print(f"{i + 1}. [{status}] {t['task']}")

def complete_task():
    task_num = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["is_complete"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        deleted = tasks.pop(task_num)
        print(f"Task '{deleted['task']}' deleted.")
    else:
        print("Invalid task number.")

def clear_all_tasks():
    confirm = input("Are you sure you want to delete all tasks? (y/n): ")
    if confirm.lower() == "y":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Clear all canceled.")


while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Clear All Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        clear_all_tasks()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")


