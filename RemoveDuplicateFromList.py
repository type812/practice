#Approach 1
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
s = [1, 2, 3]

print(list(set(t) - set(s)))
#Maintaining order
from collections import OrderedDict
print(list(OrderedDict.fromkeys(t)))

#Approach 2

myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []
[cleanlist.append(x) for x in myList if x not in cleanlist]