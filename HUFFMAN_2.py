
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


def push_item(lis,item):
        return lis.append(item)   

def mapping(root):    
####### IN-ORDER TRAVERSE with RECURSION
#def in_order_with_recursion(tree):
    letters = []
    maps = {}
    binare =""
    code = list()
    while root:
        if root.has_left():
            node = root.get_left_child()
            while node:
                if node.has_left():
                    code.append(str(node.label))
                    letters.append(node.value)
                    letter = letters.pop()
                    l_code = binare.join(code)
                    if not node.get_left_child().has_left():            
                        node.get_left_child().value
                        code.append(str(node.get_left_child().label))
                        letters.append(node.get_left_child().value)
                        letter = letters.pop()
                        l_code = binare.join(code)              
                        node.set_left_child(None)
                        maps[letter] = l_code
                        code.pop()
                        l_code = ""
                    else:
                        node = node.get_left_child()
                elif node:

                        node.get_label()
                        code.append(str(node.get_right_child().label))
                        letters.append(node.get_right_child().value)
                        letter = letters.pop()
                        l_code = binare.join(code)              
                        node.set_right_child(None)
                        maps[letter] = l_code
                        code.clear()
                        l_code = ""
                        node = None
        elif root.get_right_child():
            node = root
            while node: 
                if node.label is not None:
                    code.append(str(node.label))
                letters.append(node.value)
                letter = letters.pop()
                l_code = binare.join(code)
                node = node.get_right_child()   
            maps[letter] = l_code
            node.set_right_child(None)
    # def traverse(node):
        
    #     if node:
    #         if node.label is not None:
    #             code.append(str(node.label))
    #         traverse(node.get_left_child())
    #         letters.append(node.value)
    #         letter = letters.pop()
    #         l_code=binare.join(code)
    #         code.clear()
    #         maps[letter] = l_code
    #         node = root
    #         traverse(node.get_right_child())
                       
    # traverse(root)
    return maps

class Tree():
    def __init__(self,value):
        self.node = HuffmanNode(value)
        self.heap = heapq
        
    def add_to_heap(self,node):
        self.heap.heappush(node)
    

    def set_node_from_two(self,left,right):
        self.value = left.value+right.value
        
    

    def get_root(self):
        return self.node


    def push_item(self,lis,item):
        return lis.append(item)
    
  
class HuffmanNode(object):
    def __init__(self,data):
        self.value = data[0]
        self.freq = data[1]
        self.left_child = data[2]
        self.right_child = data[3]
        self.label = None

    def set_left_child(self,value):
        self.left_child = value

    def get_left_child(self):
        return self.left_child

    def set_right_child(self,value):
        self.right_child = value

    def get_right_child(self):
        return self.right_child

    def set_node_value(self,value):
        self.value = value
    
    def get_node_value(self):
        return self.value
    
    def set_node_frequency(self,left,right):
        self.freq = self.get_freq(left)+self.get_freq(right)

    def get_freq(self,data):
        return data[1]

    def set_label(self,label):
        self.label = label

    def get_label(self):
        return self.label

    def has_left(self):
        return self.left_child is not None

    def has_right(self):
        return self.right_child is not None  

    
def huffman_encoding(data):
   
    if data is None:
        return -1
    char_occurence = occurence(data)
    nodes_list = []
    
    for k,v in char_occurence.items():

        nodes_list.append((k,v,None,None))
    

    # s_list = sorted(char_occurence.items(),key=lambda key:key[1])
    s_list = nodes_list
    # tree = Tree(value,freq)
    while len(s_list)>1:
        s_list = sorted(s_list,key=lambda key:key[1])
        left = s_list.pop(0)
        left = HuffmanNode(left)
        left.set_label(0)
        right = s_list.pop(0)
        right = HuffmanNode(right)
        right.set_label(1)
        joint_freq = left.freq+right.freq
        joint_node = ("",joint_freq,left,right)
        push_item(s_list,joint_node)
    root = HuffmanNode(joint_node)                
    encoded = mapping(root)
    return root,encoded

    
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
