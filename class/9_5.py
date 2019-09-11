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



user_1 = User('luu', 'lau', '18')
user_1.describe_user()
user_1.greet_user()

user_2 = User('haha', 'hehe', '1080')
user_2.describe_user()
user_2.greet_user()
user_2.increment_login_attempts()
user_2.reset_login_attempts()
