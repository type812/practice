'''
e.g:
I apple peel
returns
I
'''
def non_repeating(s):
    s = s.replace(' ','').lower()
    char_count={}

    for c in s:
        if c in char_count:
            char_count[c] +=1
        else:
            char_count[c] = 1

    for c in s:
        if char_count[c]==1:
            return c
    return None

print(non_repeating('I apple peel'))
