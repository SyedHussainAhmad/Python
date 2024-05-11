n1= int(input("Enter First Number\n"))
n2= int(input("Enter Second Number\n"))
n3= int(input("Enter Third Number\n"))
n4= int(input("Enter Fourth Number\n"))

if (n1>n2 and n1>n3 and n1>n4):
    print (n1,"is greatest")
elif ( n2>n1 and n2>n3 and n2>n4):
    print (n2,"is greatest")
elif ( n3>n1 and n3>n2 and n3>n4):
    print (n3,"is greatest")
elif ( n4>n1 and n1>n3 and n4>n2):
    print (n2,"is greatest")
else :
    print ("invalid")
