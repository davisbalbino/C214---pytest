class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if any(u.user_id == user.user_id for u in self.users):
            raise ValueError("User already exists")
        self.users.append(user)

    def get_user(self, user_id):
        return next((u for u in self.users if u.user_id == user_id), None)

    def get_all_users(self):
        return self.users

    def remove_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
        else:
            raise ValueError("User not found")
