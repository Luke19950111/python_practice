def make_sandwich(*mix):
    print('You want a sandwich with:')
    for i in mix:
        print('\t-' + i)

make_sandwich('1', '2')
make_sandwich('haha', 'hehe', 'lala')
make_sandwich('water', 'water')