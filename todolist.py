#todo-list

tasks = []
def add_task():
    while True:
        task = input("Enter a task: ")

        if not task.strip():
            break

        new_task = {
            "task": task,
            "completed": False,
        }

        tasks.append(new_task)
        print("Task added!")


def view_tasks():
         if not tasks :
             print("Your task list is empty!")
         else:
             for number, task in enumerate(tasks, start=1):
                status = "done" if task["completed"] else " "

                print(f"{number}. [{status}] {task['task']}")


def mark_completed():
    view_tasks()

    if not tasks :
        return

    try:
        task_number = int(input("Enter task number to mark completed: "))

    except ValueError:
        print("Please enter a valid task number!")
        return


    if 1 <= task_number <= len(tasks):
        selected_task = tasks[task_number - 1]
        selected_task["completed"] = True
        print("Task marked as completed!")

    else:
        print("Invalid task number!")


def delete_task():
    view_tasks()

    if not tasks :
        return

    try:
        task_number = int(input("Enter task number to delete: "))

    except ValueError:
        print("Please enter a valid task number!")
        return

    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted!")

    else:
        print("Invalid task number!")


while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark completed")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using this program!")
        break

    else:
        print("Invalid choice! Try again!")


