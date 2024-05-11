def divisible(x): return x % 5 == 0

list1 = [1, 2, 32534, 7456, 42345, 758, 24543, 44445, 465]

value = filter(divisible, list1)

print(list(value))