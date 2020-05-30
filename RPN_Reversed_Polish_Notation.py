class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    # TODO: Iterate over elements 
    stack = Stack()
    if input_list is None:
        return False
    else:
        expr = input_list
        for each in expr:
            if each not in ['+','-','*','/']:
                stack.push(each)
            else:
                if each == "+":
                    last = int(stack.pop())
                    pre = int(stack.pop())
                    new_last = pre+last
                    stack.push(new_last)
                    
                elif each == "-":
                    last = int(stack.pop())
                    pre = int(stack.pop())
                    new_last = pre-last
                    stack.push(new_last)
                    
                elif each == "*":
                    last = int(stack.pop())
                    pre = int(stack.pop())
                    new_last = pre*last
                    stack.push(new_last)
                    
                elif each == "/":
                    last = int(stack.pop())
                    pre = int(stack.pop())
                    new_last = int(pre/last)
                    stack.push(new_last)
                    
             
    return new_last                        
    # TODO: Use stacks to control the element positions
    
def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]

test_function(test_case_1)