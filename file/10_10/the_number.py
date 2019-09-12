filename = 'what.txt'
with open(filename, encoding='UTF-8') as f_obj:
    contents = f_obj.read()

    the_number = contents.count('the')
    the_lower = contents.lower().count('the')
    print(the_number)
    print(the_lower)