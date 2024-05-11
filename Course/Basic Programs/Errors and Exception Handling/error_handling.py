try:
    num = int(input ("Enter any number: "))
    reciprocal = 1/num
    print (f'The reciprocal of {num} is {reciprocal}.')

except ValueError as e:
    print('You have entered invalid value please try a number..')

except ZeroDivisionError as e:
    print('Please make sure you are not dividing by zero.')

else:
    print ('Thanks for using my code..')
