class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __repr__(self):
        return f"User('{self.user_id}', '{self.name}')"
