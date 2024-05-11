def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b:
        return c

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
num3 = int(input("Enter third numbe\n"))
d = greatest(num1,num2,num3)
print (f'The greatest number is {d}')
