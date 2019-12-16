#solution 1
s = "asl # $ #% ^#@$### daks ldka lskdla"
print(set(s))
j = {i:s.count(i) for i in set(s)}

print(j)

#solution 2
v = 'aabcdfegh'
t= {}
for i in v:
    if i in t:
        t[i] = t[i] + 1
    else:
        t[i] = 1
print(t)