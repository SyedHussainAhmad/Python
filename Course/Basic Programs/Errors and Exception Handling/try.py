while (True):
    print("Enter 'q' to quit.. ")

    num = input ('Please Enter any number\n')

    if num is 'q':
        break
    
    try:
        num = int (num)
        if num> 10:
            print('Greater than 10..')
    
    except Exception as e:
        print ('You have provided invalid input. Please try a number.')
        

print ('Thanks for playing the game..')