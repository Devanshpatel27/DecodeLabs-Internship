# To-Do List Project

# Store tasks in list
my_tasks = []

# Function to add task
def add_task():

    task = input("Enter your task: ")

    my_tasks.append(task)

    print("Task added successfully!\n")


# Function to view tasks
def view_tasks():

    if len(my_tasks) == 0:

        print("No tasks available.\n")

    else:

        print("\nYour Tasks:")

        # Professional display using enumerate()
        for index, task in enumerate(my_tasks, start=1):

            print(f"{index}. {task}")

        print()


# Main function
def main():

    while True:

        print("===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # Add task
        if choice == "1":

            add_task()

        # View tasks
        elif choice == "2":

            view_tasks()

        # Exit program
        elif choice == "3":

            print("Goodbye!")

            break

        else:

            print("Invalid choice! Try again.\n")


# Program starting point
if __name__ == "__main__":

    main()