# n! = 1x2x3x4x5.....n

n= int (input ('Enter number to find factorial\n'))

factor=1

for i in range (1,n+1):
    factor=factor*i

print(f'The Factorial of {n} is {factor}.')

