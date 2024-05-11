def convert (cm):
    cm = cm/2.54
    return cm 

num = int (input('Enter am value to convert it into inches:\n'))
m =convert(num) 
print (f'The value of {num} is {m}')
