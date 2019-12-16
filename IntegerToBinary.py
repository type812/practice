from Stack import Stack

def intTOBin(number):
    s = Stack()

    while number > 0:
        n = number %2
        s.push(n)
        number = number // 2

    binNum = ""
    while not s.is_empty():
        binNum += str(s.pop())
    return binNum

print(intTOBin(243))
