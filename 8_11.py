def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magician = 'the Great ' + current_magician
        great_magicians.append(great_magician)
    print (great_magicians)

magicians = ['m1', 'm2', 'm3']
great_magicians = []
make_great(magicians[:], great_magicians)
print(magicians)