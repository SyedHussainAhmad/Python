def factorial(n):
    factor=1
    for i in range (1,fact+1):
        factor = factor*i
    return factor

fact = int(input ('Enter any number\n'))

f = factorial(fact)
print (f)