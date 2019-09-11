class User():
    def __init__(self, first, last, age='', gender=''):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print('first_name: ' + self.first_name)
        print('last_name: ' + self.last_name)
        if self.age:
            print('age: ' + self.age)
        if self.gender:
            print('gender' + self.gender)

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' +  self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first, last, age='', gender=''):
        super().__init__(first, last, age, gender)
        self.privileges = Privileges()



