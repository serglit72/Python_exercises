class Node (object):
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_val(self):
        return self.value

    def set_value(self,data):
        self.value = data

    def set_left_child(self,node):
        self.left = node

    def set_right_child(self,node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left(self):
        return self.left != None

    def has_right(self):
       return self.right != None

    def __repr__(self):
        return f"Node({self.get_val()})"

    def __str__(self):
        return f"Node({self.get_val()})"

class Tree(object):
    def __init__(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root
        
        
#################   TRAVERSE a tree DFS   ###################

class State(object): #we need to keep track of the state where we have visited and where have NOT      
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

######################### PRE_ORDER with STACK 
class StackNode():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def push(self,data):
        new_node = StackNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is EMPTY")
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp


##### function to TRAVERSE THE TREE DFS (Deep-First-Search)

def pre_order_with_stack(tree, debug_mode=True):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_val())
    state = State(node)
    stack.push(state)
    count = 0
    while (node):
        count+=1
        if (node.has_left() and state.get_visited_left()==False):
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_val())
            state = State(node)
            stack.push(state)


        elif node.has_right() and state.get_visited_right()==False:
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_val())
            state = State(node)
            stack.push(state)

        else:
            stack.pop()
            if stack.head is not None:
                state = stack.top()
                node = state.get_node()
            else:
                node = None
    if debug_mode:
        print(f"""
        loop count: {count}
        current node: {node}
        stack: {stack}
        """)
    return visit_order        

###### PRE-ORDER traverse with RECURSION:

def pre_order_with_recursion(tree):
    visit_order = list()
    root = tree.get_root()
   

    def traverse(node):

        if node:
            visit_order.append(node.get_val())
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
            visit_order.append(node.get_val())   
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
            visit_order.append(node.get_val()) 
            
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

# print(pre_order_with_stack(tree)) #[5, 4, 1, 7]
# print(pre_order_with_recursion(tree)) #[5, 4, 1, 7]
print(in_order_with_recursion(tree)) #[1, 4, 5, 7]
print(post_order_with_recursion(tree)) #[1, 4, 7, 5]