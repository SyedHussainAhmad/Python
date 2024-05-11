# Here we have created user defined function named perc.

def perc(marks):
    p=(sum(marks)/400)*100
    return p

marks = [60,48,66,71]
percentage = perc(marks)
print (percentage)