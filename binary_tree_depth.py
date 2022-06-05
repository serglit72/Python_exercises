import math
import os
import random
import re
import sys

class BinarySearchTreeNode:
    def __init__(self, node_data):
        self.data = node_data
        self.left = None
        self.right = None

def insert_node_into_binary_search_tree(node, node_data):
    if node == None:
        node = BinarySearchTreeNode(node_data)
    else:
        if (node_data <= node.data):
            node.left = insert_node_into_binary_search_tree(node.left, node_data)
        else:
            node.right = insert_node_into_binary_search_tree(node.right, node_data)

    return node

def print_binary_search_tree_inorder_traversal(node, sep, fptr):
    if node == None:
        return

    print_binary_search_tree_inorder_traversal(node.left, sep, fptr)

    if node.left:
        fptr.write(sep)
    fptr.write(str(node.data))

    if node.right:
        fptr.write(sep)

    print_binary_search_tree_inorder_traversal(node.right, sep, fptr)

#
# Complete the 'maxDepth' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_BINARY_SEARCH_TREE root as parameter.
#

#
# For your reference:
#
# BinarySearchTreeNode:
#     int data
#     BinarySearchTreeNode left
#     BinarySearchTreeNode right
#
#

def maxDepth(root):
    #
    # Write your code here
    # Function should return only one number - answer
    #
    node = root
    depth_l = 0
    depth_r = 0
    max_d = []
    if root == None: return -1
    
    while root:
        if root.left != None:
            depth_l +=1
            max_d.append(depth_l)
            root = root.left
        elif root.right:
            depth_r +=1
            max_d.append(depth_r)
            root = root.right
        else:
            #print (max(max_d))
            if len(max_d)==0:  return 0
            
            #print (max(max_d))
            
            return (max(max_d))
        
    

    # while(node):
    #     continue

    # return
    
    
    
if __name__ == '__main__':
  
    binary_search_tree_count = 12

    binary_search_tree = None
    with open('OUTPUT_PATH.txt','w') as fptr:
        fptr.write(str(binary_search_tree) + '\n')
    binary_search_tree_item = []
    
    for each in binary_search_tree_item:
        binary_search_tree = insert_node_into_binary_search_tree(binary_search_tree, each)
    
    
    maxDepth(binary_search_tree)
    # print_binary_search_tree_inorder_traversal(binary_search_tree, '|', fptr)
    
    
