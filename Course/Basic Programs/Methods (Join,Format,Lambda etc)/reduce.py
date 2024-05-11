from functools import reduce

def add(a, b): return a+b

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reduce(add, list1))