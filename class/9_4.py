class Restaruant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Welcome to ' + self.restaurant_name + '!')
        print('Our cuisine is ' + self.cuisine_type)
        print(str(self.number_served) + ' people have been served!')

    def open_restaurant(self):
        print('Opining!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


my_restaurant = Restaruant('R1', 'Food1')
my_restaurant.describe_restaurant()

my_restaurant.number_served = 23
my_restaurant.describe_restaurant()

restaurant_2 = Restaruant('R2', 'Food2')
restaurant_2.describe_restaurant()
restaurant_2.set_number_served(18)
restaurant_2.describe_restaurant()
restaurant_2.increment_number_served(1)
restaurant_2.describe_restaurant()



