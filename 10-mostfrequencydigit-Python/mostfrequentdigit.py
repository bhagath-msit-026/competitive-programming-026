# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def frequent(d,n):
    c=0
    while (n!=0):
        if n%10==d:
            c+=1
        n=n//10
    return c

def mostfrequentdigit(n):
    bigger=0
    for f in range (10):
        if frequent(f,n)>frequent(bigger,n):
            bigger=f
    return bigger