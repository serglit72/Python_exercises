def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    
    '''
    total = len(array)
    lower_index,mid_index,upper_index = 0,total//2,total-1
    mid_value = array[mid_index]
    
    while lower_index<=upper_index:
        mid_index = (lower_index+upper_index)//2
        mid_value = array[mid_index]
        if target == mid_value:
            return mid_index
        if target>mid_value:
            lower_index = mid_index+1  
        elif target<mid_value: 
            upper_index = mid_index-1
        else:
            return mid_index
    
    return -1
print(binary_search([1,3,4,6,7,8,9,11,15,17,19,21],18))

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)



def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start_index > end_index:
        return -1
    mid_index = (start_index+end_index)//2
    mid_value = array[mid_index]
    if mid_value == target:
        return mid_index
    elif target < mid_value:
       return binary_search_recursive(array, target, start_index,mid_index - 1) 
    else:
        return binary_search_recursive(array, target, mid_index+1, end_index)

def test_function1(test_case):
    answer = binary_search_recursive(test_case1[0],test_case1[1],0,9)
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target1 = 4
index1 = 4
test_case1 = [array1, target1,index1]

test_function1(test_case1)