'''
num =[1,2,3]

inum = iter(num)

while True:
    try:
        item = next(inum)
        print(item)
    except StopIteration:
        break
'''
'''
Implementation of range function 
'''

class MyRange:

    def __init__(self,start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current

def myRangeCount(start, end):
    current = start
    while current < end:
        yield current
        current +=1

obj = MyRange(1,10)

print(next(obj))
#obj.myRangeCount(1,10)


