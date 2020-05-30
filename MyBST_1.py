
def binary_search_1(array,target):
    
    if len(array) == 0:
        return -1

    left, right = 0, len(array)-1
   
    while left <= right :
        middle = (left+right)//2

        if array[middle] == target:
            return middle
    
        elif array[middle] < target:
            left = middle+1
        
        else:
            right = middle-1

    return -1
  
array =  [-1,0,1,3,7,11,19,31,54,61,80]
target = 7
index = binary_search_1(array,target)
print("index = ", index)