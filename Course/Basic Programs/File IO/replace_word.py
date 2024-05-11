with open ('donkey.txt','r') as f:
    file = f.read()

a= file.replace('donkey','#####')

with open ('donkey.txt','w') as f:
    f.write(str(a))