# Python3 program to reverse a string
# s = input()
s = "I work at Amazon"
words = s.split(' ')
string =[]
for w in reversed(words):
    string.append(w)

print(' '.join(string))


# Solution proposed by Ankit
