a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

try:
    c = a/b
    print (f'{a}/{b} is {c}.')

except ZeroDivisionError as e:
    print ('Infinite..')