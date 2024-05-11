def increment(num):
    try:
        return int(num)+1
    
    except:
        raise ValueError('Make sure you have entered a number..')


value = increment(input('Enter any number: '))
print (f'The incremented value is {value}')

    