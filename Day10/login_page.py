class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        print(f"Entering Username: {username}")

    def enter_password(self, password):
        print(f"Entering Password: {password}")

    def click_login(self):
        print("Clicking Login Button")