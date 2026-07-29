from objective import Todo
from objective import Todo
from task import Task
from datetime import date, datetime


def create_task():
    name = input("Task name: ")
    task_type = input("Task type: ")
    allocated_time = int(input("Allocated hours: "))

    due_date = datetime.strptime(
        input("Due date (dd/mm/yyyy): "),
        "%d/%m/%Y"
    ).date()

    task = Todo(
        action_name=name,
        action_type=task_type,
        allocated_time=allocated_time,
        action_due_date=due_date,
    )

    task.insert_task()

    print(f"Task created with ID {task.action_id}")

database = Todo("", "", 0, "01/01/2000")

def show_tasks():
    tasks = database.get_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(task)


def update_task():
    database.update_task()


def delete_task():
    database.delete_task()


def complete_task():
    database.complete_task()


def determine_priority():
    temp = Todo("", "", 0, "01/01/2000")
    tasks = temp.get_tasks()

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(task)

    task_id = int(input("Which task would you like to evaluate? "))

    for task in tasks:
        if task.action_id == task_id:

            priority_task = Task(
                action_name=task.action_name,
                action_type=task.action_type,
                allocated_time=task.allocated_time,
                action_due_date=task.action_due_date,
                action_completed=task.action_completed,
                action_id=task.action_id,
            )

            score = priority_task.determine_priority()

            print(f"\nPriority Score: {score}")
            return

    print("Task not found.")


def main():

    while True:

        print("\n========== TODO APP ==========")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Determine Task Priority")
        print("7. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            create_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            complete_task()

        elif choice == "6":
            determine_priority()

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()