def make_great(magicians):
    for i in range(0,len(magicians)):
        magicians[i] = 'the Great ' + magicians[i]
    print (magicians)

magicians = ['m1', 'm2', 'm3']
make_great(magicians)