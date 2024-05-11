letter = '''Good Evening <|Name|>,
Greetings from ABC Company
             you are selected !
             <|Date|>
             CONGRATULATIONS!
'''
a=input("Please Enter your name\n") 
b= input ("Please Enter Date\n")
letter = letter.replace("<|Name|>",a)
letter = letter.replace("<|Date|>",b)
print (letter)