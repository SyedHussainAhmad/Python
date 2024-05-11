import time

initial = time.time()

n=1 
while n<5:
    print("You are awesome..")
    n= n+1

print (f"Time taken by while loop is {time.time()-initial} Seconds")

initial2 = time.time()

for i in range (4):
    print("You are perfect..")

print (f"Time taken by for loop is {time.time() - initial2} Seconds")