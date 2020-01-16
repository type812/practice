'''
give a string reverse all words
Eg.
'cat bat sat'
to
'sat bat cat'
'''
def reverseStr(s):
    #return ' '.join(reversed(s.split()))
    return ' '.join(s.split()[::-1])

print(reverseStr('cat bat sat'))