# middle value index from array of [1,3,2] - value 2 has index 2
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

# basic_op('+', 4, 7)         # Output: 11
# basic_op('-', 15, 18)       # Output: -3
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

# to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable.\
#  Implement a function that will return minimum number of breaks needed.
def breakChocolate(n, m):
    return n*m-1 if (n > 0 and m > 0) else 0