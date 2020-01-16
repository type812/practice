'''
given a string ,are all characters unique?
should return True or False
'''

def unique(str):
    str = str.replace(' ','')
    return len(set(str))== len(str)

print(unique('a bcd e')) #True
print(unique('a bcd eee')) #False 