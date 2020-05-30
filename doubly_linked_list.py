class Node:
     
    def __init__(self,data=0):
        self.data = data
        self.next = None
        self.prev = None
    
    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data

class DoublyLinkedList(object):
    
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size
    
    def insert_end(self, data): # attaching new node to the end of the DLL
        
        if self.head is None:
            self.head = Node(data)
            print('This node {} is created as HEAD',format(self.head.data))
            return

        n = self.head
        while n.next:
            n = n.next
        
        new_node = Node(data)
        
        n.next = new_node
        new_node.prev = n
      
    def insert_start(self,data):  # pushing new node to the upfront of the DLL
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            print(self.head.get_next(),self.head.get_data(),self.head.get_prev())
            return 

        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_after(self,value,data): # we will insert new node after the "value" if DDL is not EMPTY and not the last one
        if self.head is None:
            print("DLL is empty")
            return
        else:
            node = self.head
            while node is not None:
                if node.data == value:
                    print("We've found the node")
                    break
                node = node.next
            if node is None:
                print("Node does not exist")
            else:
                new_node = Node(data)
                new_node.prev = node
                new_node.next = node.next
                if node.next is not None:
                    node.next.prev = new_node
                node.next = new_node
    
    def is_empty(self):
        if self.head is None:
            print("DLL is empty")
            return True

    def ssize(self):
        if not self.is_empty():
        
            n = self.head
            while n.next is not None:
                n = n.next
                self.size +=1
            return(self.size)
        else:
            return -1

    def start_delete(self):
        if self.is_empty():
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def end_delete(self):
        if self.is_empty():
            return
        if self.head.next is None:
            self.head = None
            return
        
        node=self.head

        while node.next is not None:
            node = node.next
        node.prev.next = None    
        
        
    def __repr__(self): # representer of the dll for strings ONLY
            node = self.head
            nodes = []
            while node is not None:
                nodes.append(node.data)
                node = node.next
            nodes.append("None")
            nodes.insert(0,"None")
            return " <-> ".join(nodes)

dll = DoublyLinkedList()
dll.start_delete()
dll.end_delete()
dll.insert_end("5")
dll.insert_end("6")
dll.insert_start("17")
print (dll)

dll.insert_after("5","8")

dll.start_delete()
dll.start_delete()
dll.end_delete()
print (dll)
s=dll.ssize()
print(s) 
# print (dll)