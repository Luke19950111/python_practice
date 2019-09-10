class Restaruant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Welcome to ' + self.restaurant_name + '!')
        print('Our cuisine is ' + self.cuisine_type)

    def open_restaurant(self):
        print('Opining!')

my_restaurant = Restaruant('r_name', 'r_food')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaruant('Horrible_R', 'Horrible_F')
your_restaurant.describe_restaurant()