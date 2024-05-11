import os

old_name = input('Enter Old name\n')
new_name = input('Enter New Name\n')

with open (old_name) as f:
    file = f.read()

with open (new_name,'w') as f:
    f.write(file)

os.remove(old_name)