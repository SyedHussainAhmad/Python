n = int(input("Enter no of lines: "))

condition = bool(int(input("Enter Type (1) or (0): "))) # --> String cannot directly type cast into Boolean.


if condition == True:
    for i in range(n):
        print ('*'*(i+1))

elif condition == False:
    for i in range(n):
        print ('*'*(n-i))