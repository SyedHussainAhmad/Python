from numpy import percentile


maths = int(input("Enter marks of maths\n") )
eng = int(input("Enter marks of eng\n") )
urdu = int(input("Enter marks of urdu\n") )
total = int(input("Enter total marks \n") )

maths_perc = (maths*100)/100
print (maths_perc)

eng_perc = (eng*100)/100 
print (eng_perc)

urdu_perc = (urdu*100)/100
print (urdu_perc)


sum = (maths+eng+urdu)
total_perc = (sum*100)/total
print (total_perc)

if (total_perc > 40 and maths_perc > 33 and eng_perc > 33 and urdu_perc > 33):
    print ("Student is pass")
else:
    print ("Student is fail")


if (total_perc>90):
    print('A+ Grade')

