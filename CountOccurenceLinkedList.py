#two classes each for node object and linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self,data):
        new_node = Node(data)
        #when list is empty
        if self.head is None:
            self.head =new_node
            return
        #when list has elements already and append this to end
        last_node = self.head
        #move and check if the head is not null
        #last_node .next go over to next and check and update the value
        while last_node.next:
            last_node = last_node.next
        #last null arrived hence assign the value.
        last_node.next = new_node
    def count_occ(self,data):
        count = 0 #initialisation of count variable
        cur = self.head  #set current node as head
        while cur:   #while current node is not null
            if cur.data == data:  #if current node's data matches with the data searched, increase count
                count+=1
            cur = cur.next      #set current to point to next node
        return count

#define Linked list object.

llist = LinkedList()

llist.append("1")
llist.append("2")
llist.append("1")
llist.append("3")
llist.append("4")
llist.append("5")
llist.append("2")
llist.append("3")
#print(llist.print_list())
#llist.prepend("E")
print(llist.count_occ("5"))
#print(llist.print_list())
