'''
Ex: 'Clint Eastwood' anagrams to 'old west action
OR
dog to god
OR
121 to 211 etc
Not Anagram:
aa & ab
'''
'''
def anagram(s1,s2):
    s1 = s1.replace(' ','').lower
    s2 = s2.replace(' ', '').lower
    #return sorted(s1) == sorted(s2)  #return True or False


#anagram('clint Eastwood','old  Westaction')
'''
#### without using inbuilt methods

def anagram_check(s1,s2):
    s1 = s1.replace(' ', '').lower
    s2 = s2.replace(' ', '').lower

    if len(s1)!=len(s2):
        return False
    #frequency counter
    c= {}

    for letter in s1:
        if letter in c:
            c[letter]+=1
        else:
            c[letter]=1
    #reverse counting for s2 string..
    for letter in s2:
        if letter in c:
            c[letter]-=1
        else:
            c[letter]=1

    for k in c:
        if c[k]!=0:
            return False
    return True

x = anagram_check("aba","baa")
print(x)