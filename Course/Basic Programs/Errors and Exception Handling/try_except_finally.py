try:
    num = int(input ("Enter any number: "))
    reciprocal = 1/num
    print (f'The reciprocal of {num} is {reciprocal}.')

except ValueError as e:
    print('You have entered invalid value please try a number..')
    exit()

except ZeroDivisionError as e:
    print('Please make sure you are not dividing by zero.')
    exit()

else:
    print('We are Successful..')

finally:
    print ('Thanks for using my code..')