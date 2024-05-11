def table (n):
    for i in range (1,11):
       print(f"{n}x{i}={n*i}")

num = int(input('Enter any number to get table:\n'))
a = table (num) 
print (a)
