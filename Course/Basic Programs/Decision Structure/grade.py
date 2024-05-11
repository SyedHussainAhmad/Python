perc = int(input("Enter Percentage\n"))

if (perc>90 and perc<100):
    print("Your Grade is A+")
elif(perc>80):
    print("Your Grade is A")
elif(perc>75):
    print("Your Grade is B+")
elif(perc>70):
    print("Your Grade is B")
elif(perc>65):
    print("Your Grade is C+")
elif(perc>60):
    print("Your Grade is C")
elif(perc>55):
    print("Your Grade is D+")
elif(perc>50):
    print("Your Grade is D")
elif(perc<50):
    print("Your Grade is F")
else:
    print("Invalid")
