class LoginCredentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def CheckUsername(self):
        if self.username == "admin":
            print("Username correct!")
        else:
            print("Username incorrect.")

    def CheckPassword(self):
        if self.password == "admin123":
            print("Password correct!")
        else:
            print("Password incorrect.")

    def login(self):
        if self.username == "admin" and self.password == "admin123":
            print("Login successful!")
        else:
            print("Login failed.")

