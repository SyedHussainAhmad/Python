def factorial_rec(n):
    if n==1 or n==0:
        return 1
    return n*factorial_rec(n-1)

m = int(input('Enter any number\n'))
fact= factorial_rec(m)
print(fact)

