
import heapq
import sys


# 1. Each character occurence counting:
def occurence(data_string):
    char_occurence = dict()
    string = data_string
    for i in string:
        if i in char_occurence:
            char_occurence[i]+=1
        else:
            char_occurence[i]=1
    return char_occurence


# 2. Build the Huffman Node by assigning two smallest frequency letter 

def find_two_smallest(lis):
   
    left = lis.pop(0)
    right = lis.pop(0)
    frequency = left[1]+right[1]
    
    return [(left,right),frequency]

# def mapping(tree):
#     binary_code = list()
#     # node = tree.get_root()
#     code=""
    
#     while tree.node: 
#         if tree.node.left_child:
#             binary_code.append('0')
#             tree.node = tree.left_child[0]
#     code.join(binary_code)
           
#         # while tree.has_right:
#         #     label = tree.get_right_label())
#         #     binary_code.append(label)
                              
#     # traverse(root)
#     return code



class Tree():
    def __init__(self,value=None):
        self.node = HuffmanNode(value)
        self.heap = []
        
    def add_to_heap(self,node):
        self.heap.append(node)

    def get_root(self):
        return self.node

    def push_item(self,lis,item):
        return lis.append(item)
    
  
class HuffmanNode(object):
    def __init__(self,left_child=None,right_child=None,frequency=None):
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child
    
    def set_left_child(self,value):
        self.left_child = value
        
    def set_right_child(self,value):
        self.right_child = value
        
    
    def get_left_label(self):
        return self.left_child[0]

    def get_right_label(self):
        return self.right_child[0]

    def has_left(self):
        return self.left_child != None

    def has_right(self):
        return self.right_child != None  


        
    
    
def huffman_encoding(data):
    #1.Transforming a given string into dictionary with (char:frequency)
    if data is None:
        return -1
    char_occurence = occurence(data)
    encoded = []
    #2.Getting a list from dictionary(character:frequency)
    s_list = sorted(char_occurence.items(),key=lambda key:key[1])
    
 
    #3.Building a HuffmanTree
    tree = Tree() #instance of the HufmanTree class
    
    #4.Merging these two smallest into new HuffmanNode and pushing it to the Tree
    while len(s_list)>1:
        
        s_list = sorted(s_list,key=lambda key:key[1])
        two_smallest = find_two_smallest(s_list)    
        new_node = HuffmanNode(two_smallest[0][0],two_smallest[0][1],two_smallest[1]) 
        tree.add_to_heap(new_node)
        tree.node = tree.heap.pop()
        tree.push_item(s_list,two_smallest)
                      
    # encoded=mapping(tree)
    return tree,encoded
    

# def huffman_decoding(s_list,tree):
    
#     if data is None:
#         print("No data")
   
#     else: 
# pass

if __name__ == "__main__":
    # codes = {}
    # a_great_sentence = "The content of the encoded data is"
    # a_great_sentence = "The bird is the word"
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
    name = sys.getrefcount(a_great_sentence)
    print(name)
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    
    encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the data is: {}\n".format(encoded_data))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))


#=================================================================================
# string = "The bird is the word"
# char = occurence(string)
# s_list = sorted_occurence_list(char)
# tree = Tree()

# print(s_list)
# print(huffman_encoding(string))





