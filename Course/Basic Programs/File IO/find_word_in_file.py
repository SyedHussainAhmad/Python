with open('log_file.txt') as f:
   content= f.read()
content = content.lower()
if 'python' in content:
    print('Yes pyhton is present')
else:
    print('No pyhton is not present')