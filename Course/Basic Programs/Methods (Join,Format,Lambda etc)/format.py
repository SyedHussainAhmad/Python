# It is an old method of f string:
tea = 'Tea'
coffee = 'Coffee'
name = input('Enter your name: ')


# a= f'Good Morning! {name}. Would you like to have some {tea} or {coffee}.'  
# --> This is a f string
# print (a)


a = 'Good Morning! {}. Would you like to have some {} or {}.'.format(name,tea,coffee)
print (a)
# --> This is a format method.

