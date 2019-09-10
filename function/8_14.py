def make_car(manufacturer, type, **options):
    car = {}
    car['manufacturer'] = manufacturer
    car['type'] = type
    for k, v in options.items():
        car[k] = v
    return car

my_car = make_car('subaru', 'outback', color='blue', two_package=True)
print(my_car)