# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
    b=[]
    for i in L:
        for j in i:
            b.append(j)
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            if (b[i]==b[j]):
                return True
    return False
print(hasduplicates([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))