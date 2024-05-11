list = ['Piya',32,8.66,True]

# index = 0
# for item in list:
#     print (f'The list item {item} is at index {index}.')
#     index += 1 
# --> this is the normal way.


for index,item in enumerate(list):
    print(f'The list item {item} is at index {index}.')

# --> this is the short way.