n1= int(input("Enter First Number\n"))
n2= int(input("Enter Second Number\n"))
n3= int(input("Enter Third Number\n"))
n4= int(input("Enter Fourth Number\n"))

if (n1>n2):
    f1 = n1
else:
    f1 = n2

if (n3>n4):
    f2 = n3
else:
    f2 = n4

if (f1>f2):
    print (f1, "is greatest")
else:
    print (f2, "is greatest")
