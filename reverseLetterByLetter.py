'''
'cat bat sat'
to
'tas tab tac'
'''
def reverEachLetter(s):
    leng = len(s)
    i = 0 #index tracker
    spaces = [' ']
    word = []
    while i< leng:
        if s[i] not in spaces:
            word_start= i

            while i<leng and s[i] not in spaces:
                i +=1
            word.append(s[word_start:i])
        i+=1
    return "".join(reversed(s))

print(reverEachLetter('this is the best'))