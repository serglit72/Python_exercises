class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    # TODO: Intiate stack object
    opens = Stack()
    closes= Stack()
    # TODO: Interate through equation checking parentheses
    expression = str(equation)
    for each in expression:
        if each == "(":
            opens.push(1)
        elif each == ")":
            closes.push(1)
    # TODO: Return True if balanced and False if not

    return (opens.size()==closes.size())
print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")