words = ['donkey','mota','monkey','pagal','ullo']

with open ('donkey.txt') as f:
    file = f.read()

for word in words:
    file= file.replace(word,'#####')
    with open ('donkey.txt','w') as f:
        f.write(str(file))