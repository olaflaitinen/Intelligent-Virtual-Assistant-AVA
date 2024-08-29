class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def execute_task(self, task_id):
        if task_id < len(self.tasks):
            task = self.tasks[task_id]
            task.execute()

class Task:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing task: {self.name}")

if __name__ == "__main__":
    manager = TaskManager()
    task = Task('Send Email')
    manager.add_task(task)
    manager.execute_task(0)
