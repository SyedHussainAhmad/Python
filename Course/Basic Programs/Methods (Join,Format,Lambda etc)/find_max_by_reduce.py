from functools import reduce

list = [1, 6, 5, 4, 8, 2, 1, 0]
value = reduce(max, list)

print(value)