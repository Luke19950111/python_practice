while True:
    why_like = input('Why do you like programming?(enter q to quit) ')
    if why_like == 'q':
        break
    else:
        print('I like programming because ' + why_like)
        filename = 'why_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(why_like + '\n')