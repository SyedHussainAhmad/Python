number = 10 # --> Global Variable..(used anywhere in the program.)

def fun1(): # --> Local Variable..(used only in the function in which it is declared.)
    global number # -->  Here it uses Global Variable.
    print(number)
    number = 12 # -->  Here it changes Global Variable as Global Variable was using.
    print (number)


fun1()
print(number)