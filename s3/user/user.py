class User:
    def __init__(self, name, password, is_admin=False):
        self.name = name
        self.password = password
        self.is_admin = is_admin
        self.is_authenticated = False

    def authenticate(self, name, password):
        self.is_authenticated = self.name == name and self.password == password
        return self.is_authenticated
