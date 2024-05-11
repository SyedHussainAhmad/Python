sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))
total = int(input("Enter total marks\n"))

perc = ((sub1+sub2+sub3)*100)/total

if ( sub1<33 or sub2<33 or sub3<33):
    print ("You are fail")
elif (perc< 40):
    print ("You are fail")
else:
    print ("Congratulations! You are Pass.. ") 

if (perc > 90):
    print ("Your Grade is A+")
