class Node (object):
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def set_left_child(self,left):
        self.left = left

    def set_right_child(self,right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left(self):
        return self.left != None

    def has_right(self):
       return self.right != None


class Tree(object):
    def __init__(self,value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root
    
    def set_root(self,value=None):
        self.root = Node(value)
        
        
#################   CHECk if DUPLICATED   ###################
    def compare(self, node, new_node):
        '''
        if new_node == node, returns 0
        if new_node < existing node , returns -1
        if new_node > existing node, returns 1

        '''
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        elif new_node.get_value() > node.get_value():
            return 1

    def insert_with_loop(self, value):
        
        node = self.get_root()
        new_node = Node(value)
        if node == None:
            self.root = new_node
            return
        while(True):
            compare_result = self.compare(node,new_node) 
            if compare_result == 0:
                node.set_value(new_node.get_value())
                break
                
            elif compare_result == -1:
                if node.has_left():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
                

            else: #compare_result == 1:
                if node.has_right():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break

    def insert_with_recursion(self,value):
        if self.get_root() == None:
            self.set_root(value)
            return
        #otherwise we use a recursion here
        self.insert_with_recursion((self.get_root()), Node(value))

    def insert_recursively(self, node, new_node):
        compare_result =  self.compare(node,new_node) 
        if compare_result == 0:
            node.set_value(new_node.get_value())
            
        elif compare_result == -1:
            if node.has_left():
                self.insert_recursively(node.get_left_child(),new_node)
            else:
                node.set_left_child(new_node)
            
            
        else: #compare_result == 1:
            if node.has_right():
                self.insert_recursively(node.get_right_child(),new_node)
            else:
                node.set_right_child(new_node)
                
      
           



        

######################### TRAVERSE with QUEUE  
from collections import deque

class Queue(object):
    def __init__(self):
        self.q = deque()

    def enque(self,value):
        self.q.appendleft(value)

    def dequ(self):
        if len(self.q)>0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

def bfs_traverse(tree):
    visit_order = list()
    q=Queue()
    #start at the ROOT node an add it to the Queue
    node = tree.get_root()
    q.enque(node) #put in the queue
    while len(q)>0: #while queue is not empty
        node = q.dequ() #pull it from the queue
        visit_order.append(node)# "visited" the node
        if node.has_left():
            q.enque(node.get_left_child())
        if node.has_right():
            q.enque(node.get_right_child())
    return (visit_order)



###### PRE-ORDER traverse with RECURSION:

def pre_order_with_recursion(tree):
    visit_order = list()
    root = tree.get_root()
   

    def traverse(node):

        if node:
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())
        

    traverse(root)
    return visit_order

####### IN-ORDER TRAVERSE with RECURSION

def in_order_with_recursion(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):

        if node:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())   
            traverse(node.get_right_child())
            
            
    traverse(root)
    return visit_order

####### POST-ORDER TRAVERSE with RECURSION

def post_order_with_recursion(tree):
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):

        if node:
            traverse(node.get_left_child())  
            traverse(node.get_right_child())
            visit_order.append(node.get_value()) 
            
    traverse(root)
    return visit_order



# tree = Tree(5)
# tree.get_root().set_left_child(Node(4))
# tree.get_root().set_right_child(Node(7))
# tree.get_root().get_left_child().set_left_child(Node(1))
###### TREE is CREATED THIS WAY
#           5
#          / \
#         4   7
#        /
#       1
###### RESULTS of TRAVERSING will output

tree = Tree()
# tree.insert_with_loop(5)
# tree.insert_with_loop(4)
# tree.insert_with_loop(1)
# tree.insert_with_loop(7)

tree.insert_with_recursion(5)
tree.insert_with_recursion(4)
tree.insert_with_recursion(1)
tree.insert_with_recursion(7)

print(pre_order_with_recursion(tree)) #[5, 4, 1, 7]
print(in_order_with_recursion(tree)) #[1, 4, 5, 7]
print(post_order_with_recursion(tree)) #[1, 4, 7, 5]
print(bfs_traverse(tree)) #[5, 4, 7, 1]