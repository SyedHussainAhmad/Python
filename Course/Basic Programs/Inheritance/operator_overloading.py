class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print("The sum is shown below: ")
        return self.num + num2.num

    def __mul__(self,num2):
        print("The product is shown below: ")
        return self.num * num2.num

    def __str__(self) :
        return f'Decimal Number {self.num}'

    def __len__(self):
        return 1

n1 = Number(4)
n2 = Number(6)

print(n1)
print(n2)

sum = n1 + n2
print (sum)

product = n1 * n2
print (product)

print(f'The length of {n1} is {len(n1)}')
print(f'The length of {n2} is {len(n2)}')