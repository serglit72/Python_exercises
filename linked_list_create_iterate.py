class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#You can also add a __repr__ to both classes to have a more helpful representation 
# of the objects:
    def __repr__(self):
            return self.data
   

# The only information you need to store for a linked list is where the list starts
#  (the head of the list). Next, create another class to represent each node
#  of the linked list:


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:      # this part is not nessessary but helps to make it FASTER
            node = Node(data=nodes.pop(0))  # so uncomment it FOR REAL task
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next


    def __repr__(self): # representer of the llist
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

        # >>> llist = LinkedList(["a", "b", "c", "d", "e"])
        # >>> llist
        # a -> b -> c -> d -> e -> None
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def append(self, data):  ### "append" is local method
        if self.head is None:
            self.head = Node(data)
            return
    
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(data)
        return

    def to_list(self):
        
        #  The function to turn Linked List into Python List
        plist = []
        node = self.head # assigned the "head" of the LinkedList 
                        #   to the first item in the plist 
     
        while node:  # == while node IS NOT None
            plist.append(node.data) #here is regular (NOT local) append method for the plist
            node = node.next
    
        return plist
           

# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")



def create_llist (input_list): # input_list can be a list ["a","b","c","d"] or dict in list
    head = None
    tail = None
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head

def print_llist (head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next
#print_llist(head)  - runs a function
