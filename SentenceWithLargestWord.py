def getMaxNrWords(S):
    max_len = 0
    for sent in S:
        max_len = max(max_len, len(sent.split()))
    return max_len


S = ["We test coders", "Give us a try", ""]

print(getMaxNrWords(S))