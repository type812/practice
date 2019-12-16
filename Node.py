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
    # move the new node's next to point to head and move the head of existing ones to next
    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        #move the head pointer to the new node
        self.head = new_node
    def insert_after_node(self,prev_node, data):
        #If there is no previous node in the list give or is empty.
        if not prev_node:
            print("prev node not in  list")
            return
        #given the location where to insert
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


#define Linked list object.

llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#print(llist.print_list())
#llist.prepend("E")
print(llist.print_list())
llist.insert_after_node(llist.head.next, "E") # A > B > E > C > D
print(llist.print_list())