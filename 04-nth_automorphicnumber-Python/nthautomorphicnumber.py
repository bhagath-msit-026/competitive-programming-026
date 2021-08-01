# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def range(n):
    squ=int(n*n)
    while n>0:
        if n%10 != squ%10:
            return False
        n=n//10
        squ=squ//10
    return True

def nthautomorphicnumbers(n):
    # Your code goes here
    h=1
    g=-1
    while(h<=abs(n)):
        g=g+1
        if(range(g)):
            h=h+1
    return g