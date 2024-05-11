# syntax open('file name', 'mode')


# f=open('hussain.text','r')--> for read 
# f=open('hussain.text','w')--> for write
f=open('hussain.text','a')#--> for append
data = f.write('May Allah bless him.Ameen')
# # print(data)--> generally used for read.
f.close()

with open('texts.txt','w') as w:
    w.write('Ma boy')

# --> It is an easy method to read, write and append etc. In thid method we do not have to close the file.
