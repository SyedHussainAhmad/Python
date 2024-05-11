# def square (x):
#     return x*x 
# --> Normal function

square = lambda x:x*x # --> Lambda Function to find a square.
add = lambda a,b,c: a+b+c # --> Lambda Function to find sum.

a = int (input('Input any number: '))
b=3
c=4
print (square(a))
print (add(a,b,c))