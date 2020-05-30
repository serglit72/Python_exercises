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

def convertToTuples(data_dict):
    mylist =  []
    for k,v in data_dict.items():
        mylist.append((v,k))
    return mylist

def occurenceToTree(mylist):
    s_list = []
    for each in mylist:
        heapq.heappush(s_list,[each])
    while len(s_list)>1:
        left_child = heapq.heappop(s_list)
        right_child = heapq.heappop(s_list)
        freq_l, label_l = left_child[0]
        freq_r,label_r = right_child[0]
        freq = freq_l+freq_r
        label = "".join([str(label_l),str(label_r)])
        node = [(freq,label),left_child,right_child]
        heapq.heappush(s_list,node)
    return s_list.pop()

def codeMapCreate(codeTree):
    codeMap = {}
    code = ''
    def traverse(codeTree,codeMap,code):
        print(codeTree)
        if  len(codeTree)==1:
            label = str(codeTree[0][1])
            codeMap[label] = code    
        else:
            freq,left_child,right_child = codeTree
            traverse(left_child,codeMap,code+'0')
            traverse(right_child,codeMap,code+'1')
    traverse(codeTree,codeMap,code)
    print(codeMap)
    return codeMap

def testMakeTree():
    print('Testing occurenceToTree()...', end='')
    mytree = occurenceToTree([(7, 'A'), (3, 'B'), (7, 'C'), (2, 'D'), (6, 'E')])

    assert(mytree == [(25, 'DBEAC'), [(11, 'DBE'), [(5, 'DB'), [(2, 'D')], [(3, 'B')]], [(6, 'E')]], [(14, 'AC'), [(7, 'A')], [(7, 'C')]]])
    print("Passed!")

def testCodeMap():
    print("Testing codeMapCreate() ...", end='')
    mytree = occurenceToTree([(7, 'A'), (3, 'B'), (7, 'C'), (2, 'D'), (6, 'E')])
    tree = codeMapCreate(mytree)
    print(tree)
    assert(codeMapCreate == {'A': '10', 'B': '001', 'C': '11', 'D': '000', 'E': '01'})
data_string = 'AAAAAAABBBCCCCCCCDDEEEEEE'
# testMakeTree()
# mytree = occurenceToTree([(7, 'A'), (3, 'B'), (7, 'C'), (2, 'D'), (6, 'E')])
# codeMapCreate(mytree)
testCodeMap()
