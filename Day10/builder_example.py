class UserBuilder:

    def __init__(self):
        self.user = {}

    def first_name(self, value):
        self.user["first_name"] = value
        return self

    def last_name(self, value):
        self.user["last_name"] = value
        return self

    def email(self, value):
        self.user["email"] = value
        return self

    def build(self):
        return self.user