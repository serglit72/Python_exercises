## reverse_string.py

def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: Write your solution here
    reversed_string =""
    length = len(our_string)
    
    for i in range(length-1,-1,-1):
        reversed_string+=our_string[i]
    return reversed_string

print(string_reverser('water'))
