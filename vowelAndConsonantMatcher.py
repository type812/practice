import re
testStr='''
aeyiuo
aeYYuo
qrcbk
aeeeee
normal
EText
extTT
'''

#pattern = re.findall(r'[aeiouy]+',testStr)
pattern = re.findall(r'\b[aeiouy]+\b',testStr)
l = list(pattern)
print(l)