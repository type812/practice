myLines = []
with open('lorem.txt','r') as f:
    for line in f:
        myLines.append(line.rstrip('\n'))

print(myLines)
