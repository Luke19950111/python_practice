from user import User
from privileges import Privileges


class Admin(User):
    def __init__(self, first, last, age='', gender=''):
        super().__init__(first, last, age, gender)
        self.privileges = Privileges()