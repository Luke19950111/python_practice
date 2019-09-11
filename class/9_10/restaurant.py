class Restaurant():
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








