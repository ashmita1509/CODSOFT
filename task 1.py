def main():
    tasks = []

    while True:
                    print("\n________To-Do List________")
                    print("1. Add Task")
                    print("2. View Tasks")
                    print("3. Remove Tasks")
                    print("4. Exit")

                    choice= input("\nEnter your choice: ")

                    if choice == "1":
                            print()
                            new_task= input("Enter a new task: ")
                            tasks.append(new_task)
                            print(f"Added task: {new_task}")

                    elif choice == "2":
                            print("\nTask list: ")
                            for i, task in enumerate(tasks):
                                    print(f"{i+1}. {task}")

                    elif choice == "3":
                            task_to_remove= input("Enter the task you want to remove: ")
                            if task_to_remove in tasks:
                                    tasks.remove(task_to_remove)
                                    print(f"Removed Task: {task_to_remove}")
                            else:
                                    print(f"{task }not found!")

                    elif choice == "4":
                            print("Exiting To-Do List")
                            break
                    
                    else:
                            print("Invalid choice!")

if __name__ == "__main__":
        main()

