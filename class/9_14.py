from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

die_6 = Die()
n = 0
while n < 10:
    die_6.roll_die()
    n += 1

die_10 = Die(10)
m = 0
while m < 10:
    die_10.roll_die()
    m+=1

die_20 = Die(20)
b = 0
while b < 10:
    die_20.roll_die()
    b+=1