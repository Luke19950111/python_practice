
while True:
    guest_name = input('Please tell me your name(enter q to quite): ')
    if guest_name == 'q':
        break
    else:
        print('Welcome, ' + guest_name + '!')
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(guest_name + '\n')




