'''Write the method vowelCount(s), that takes a string s, 
// and returns the number of vowels in s, ignoring case, 
// so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).
'''

def vowelCount(s):
    count=0
    
    for i in range(len(s)):
        if("a"==s[i] or "e"==s[i] or "i"==s[i] or "o"==s[i] or "u"==s[i]):
            count=count+1
    return count
print(vowelCount("aercious"))