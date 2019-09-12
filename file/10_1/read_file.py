file_name = 'learning_python.txt'
with open(file_name) as file_object:
    # contents = file_object.read()
    # print(contents)

    # for line in file_object:
        # print(line)

    lines = file_object.readlines()

print(lines)