#This program is designed to serve as a todo list application

def choices():
  tasks = []

  while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Please enter your choice: ")

    if choice == "1":
      task = input("Input the task: ")
      tasks.append(task)
      print("Task added!")
    elif choice == "2":
      print("Tasks:")
      for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    elif choice == "3":
      view_tasks()
      task_index = int(input("Enter the task number to remove: ")) - 1
      if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Removed: (removed_task")
      else:
        print("Invalid task number.")
    elif choice == "4":
      print("Hasta la Vista!")
      break
    else:
      print("Invalid choice, please use a different choice")


choices()