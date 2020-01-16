from re import search
def check_substring(str, sub):
    #using regex
    if search(sub,str):
        print('Found')
    else:
        print('not found')

check_substring('stackabuse','tack')
