
class User:
    def __init__(self, first_name, last_name, password, hair_colour):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.hair_colour = hair_colour
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} has {self.hair_colour} hair and the user password is {self.password}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} and welcome!")

