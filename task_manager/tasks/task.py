class Task:
    _id_counter = 1

    def __init__(self, title, description):
        self.task_id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.completed = False
        self.assigned_to = None

    def mark_as_completed(self):
        self.completed = True

    def assign_to(self, user):
        self.assigned_to = user

    def __repr__(self):
        return f"Task('{self.title}', '{self.description}', completed={self.completed}, task_id={self.task_id})"
