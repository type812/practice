class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items ==[]

c = Stack()
c.push('A')
c.push('B')
c.push('C')
c.push('D')
#print(c.get_stack())
c.pop()
#print(c.get_stack())
#c.pop('B')
#c.pop('C')
#c.pop('D')
#print(c.is_empty())

