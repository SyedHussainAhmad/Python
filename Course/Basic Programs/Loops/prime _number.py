# Program to check if the given num is prime or not.

def primeNumber(n): # --> Function to check whether the number is prime or not.
    prime = True
    for num in range(2,n):
        if n%num==0:
            prime=False
            break
    if prime:
        print ('This is a prime number.')

    else:
        print ('This is not a prime number.')

if __name__ == "__main__":
    n = int (input("Enter any number to check if it is prime or not: "))
    primen = primeNumber(n) # --> Function call.

