with open ('hussain.txt') as f:
    content_1 = f.read()
with open ('texts.txt') as f:
    content_2 = f.read()

if content_1==content_2:
    print('Files are identical')
else:
    print('Files are not identical')

