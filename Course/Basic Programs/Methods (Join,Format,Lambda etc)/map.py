# To print list that contain the cube for ech item in list1.

def cube(x): return x*x*x


list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Method 1:

list2 = []
for item in list1:
    list2.append(cube(item))
print(list2)  # --> This is the normal way.

# Method 2:

print(list(map(cube, list1)))  # --> This is the short cut using map.
