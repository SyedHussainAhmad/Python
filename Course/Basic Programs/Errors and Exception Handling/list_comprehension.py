list = [2,4,6,8,10,12123,525,856,5436,97,55,45,456,24]

# Example 1:
# list1= []
# for item in list:
#     if item%2==0:
#         list1.append(item)

# print (f'Even items of the list are {list1}.') 
# --> This is the normal way.

# List with even items.
list1 = [item for item in list if item%2==0]
print (f'Even items of the list are {list1}.')
# --> This is the short way.


# Example 2:
# List with items greater than 10.
list2 = [item for item in list if item>10]
print (f'Items of the list greater than 10 are {list2}.')