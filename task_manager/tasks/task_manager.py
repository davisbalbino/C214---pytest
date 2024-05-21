class TaskManager:
    def __init__(self, user_manager):
        self.tasks = []
        self.user_manager = user_manager

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def assign_task_to_user(self, task_id, user_id):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        user = self.user_manager.get_user(user_id)
        if task and user:
            task.assign_to(user)
            user.add_task(task)
        else:
            raise ValueError("Task or User not found")
