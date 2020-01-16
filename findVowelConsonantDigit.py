f=open('lorem.txt','r')
vowels = set("AEIOUaeiou")
cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

countV = 0
countC = 0
for c in f.read():
    if c in vowels:
        countV += 1
    elif c in cons:
        countC += 1
    else:
        pass

print('Vowels are {} in number '.format(countV))
print('Consonants are {} in number '.format(countC))