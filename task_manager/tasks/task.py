# tasks/task.py
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task('{self.title}', '{self.description}', completed={self.completed})"
