def main():
  # Initialize an empty list to store tasks
  tasks = []

  while True:
    # Print the menu options
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task Done")
    print("4. update task")
    print("5. Exit")

    # Get user input
    choice = input("Enter your choice: ")

    # Handle user choices
    if choice == '1':
      task = input("Enter the task: ")
      tasks.append(task)
      print(f"Task '{task}' added successfully!")
    elif choice == '2':
      if tasks:
        print("\nTasks:")
        for index, task in enumerate(tasks):
          print(f"{index + 1}. {task}")
      else:
        print("There are no tasks in the list.")
    elif choice == '3':
      if tasks:
        print("\nTasks:")
        for index, task in enumerate(tasks):
          print(f"{index + 1}. {task}")
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
          tasks[task_index] = f"[DONE] {tasks[task_index]}"
          print("Task marked as done!")
        else:
          print("Invalid task number.")
      else:
        print("There are no tasks in the list.")
    elif choice == '4':
        if tasks:
            print("\nTasks:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            task_index = int(input("Enter the task number to be updated: ")) - 1
            if 0 <= task_index < len(tasks):
                new_task = input("Enter the new task: ").strip()
                if new_task:
                    old_task = tasks[task_index]
                    tasks[task_index] = new_task
                    tasks.append(task)
                    print(f"Updated: '{old_task}' to '{new_task}'")
                else:
                    print("New task cannot be empty.")
            else:
                print("Invalid number.")



    elif choice == '5':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
