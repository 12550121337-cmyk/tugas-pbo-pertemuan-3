class User:
    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.login_attempts = 0  

    def describe_user(self):
        print(f"User full name is {self.first_name} {self.last_name}.")
        print(f"This user lives in {self.city}.")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

    
    def increment_login_attempts(self):
        self.login_attempts += 1

    
    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('Hanifah', 'Afrilia', 'PekanBaru')

print(f"The user first name is {user.first_name}.")
print(f"The user last name is {user.last_name}.")
print(f"The user lives in {user.city}.")
user.describe_user()
user.greet_user()


user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login attempts: {user.login_attempts}")


user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
print()
