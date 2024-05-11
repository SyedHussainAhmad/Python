def sums (n):
    if n==0:
        return 0
    return n+sums(n-1)

num = int(input('Enter any number till then you want sum:\n'))
m=sums(num)
print ('Your sum is',m)