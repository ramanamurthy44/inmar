class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task: str):
        if task not in self.tasks:
            self.tasks[task] = False  # False indicates the task is not completed
        else:
            print(f"Task '{task}' already exists.")

    def remove_task(self, task: str):
        if task in self.tasks:
            del self.tasks[task]
        else:
            print(f"Task '{task}' does not exist.")

    def get_tasks(self):
        return [{'task': task, 'completed': completed} for task, completed in self.tasks.items()]

    def complete_task(self, task: str):
        if task in self.tasks:
            self.tasks[task] = True  # Mark the task as completed
        else:
            print(f"Task '{task}' does not exist.")

todo_list = ToDoList()

# Add some tasks
todo_list.add_task("Buy groceries")
todo_list.add_task("Read a book")
todo_list.add_task("Go for a walk")

# Try to add a duplicate task
todo_list.add_task("Buy groceries")

# Complete a task
todo_list.complete_task("Read a book")

# Remove a task
todo_list.remove_task("Go for a walk")

# Try to remove a non-existent task
todo_list.remove_task("Go for a walk")

# Get and print all tasks
tasks = todo_list.get_tasks()
print(tasks)