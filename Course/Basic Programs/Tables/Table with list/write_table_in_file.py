n = int(input('Enter any number to get table in the list: '))

table = [n*i for i in range (1,11)]
print(str(table))

with open('table.txt','a') as f:
    f.write(f'{table}\n')