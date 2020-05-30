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
        
        
#################   TRAVERSE a tree BFS   ###################



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
    return visit_order



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



tree = Tree(5)
tree.get_root().set_left_child(Node(4))
tree.get_root().set_right_child(Node(7))
tree.get_root().get_left_child().set_left_child(Node(1))
###### TREE is CREATED THIS WAY
#           5
#          / \
#         4   7
#        /
#       1
###### RESULTS of TRAVERSING will output


print(pre_order_with_recursion(tree)) #[5, 4, 1, 7]
print(in_order_with_recursion(tree)) #[1, 4, 5, 7]
print(post_order_with_recursion(tree)) #[1, 4, 7, 5]
print(bfs_traverse(tree)) #[5, 4, 7, 1]