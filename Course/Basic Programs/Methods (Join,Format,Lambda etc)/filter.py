def greater(num):
    if num > 5:
        return True
    else:
        return False

findGreater = lambda num: num>10

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6457, 367, 234, 5678, 978]

print (list(filter(greater,list1))) 
# --> Prints all the numbers greater than 5.

print (list(filter(findGreater,list1))) 
# --> Prints all the numbers greater than 10.