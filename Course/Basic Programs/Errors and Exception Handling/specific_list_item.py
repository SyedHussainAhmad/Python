list = ['Piya', 32, 8.66, True, 'Atif', 3, 2342, 'Mango']

for index, item in enumerate(list):
    if index == 2 or index == 4 or index == 6:
        if index == 2:
            print(f'The {index+1}rd element of the list is {item}.')
        else:
            print(f'The {index+1}th element of the list is {item}.')
