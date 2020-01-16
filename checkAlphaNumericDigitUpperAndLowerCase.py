#any ->
def check():
    S = input('Enter string: ')

    print(any(map(str.isdigit,S)))

check()