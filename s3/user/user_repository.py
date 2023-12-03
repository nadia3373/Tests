class UserRepository:
    def __init__(self):
        self.data = []

    def add_user(self, user):
        self.data.append(user)

    def find_by_name(self, username):
        return any(user.name == username for user in self.data)

    def logout_all_except_admins(self):
        for user in self.data:
            if not user.is_admin:
                user.is_authenticated = False
