#my solution
# def count_hi(str):
#   result = 0
#   l = len(str)
#   if l<2:
#     return 0
  
#   for i in range(l):
#     if (str[i] == "h" and str[i+1] == "i"):
#       result +=1
#   return result

#optimal solution
def count_hi(str):
    sum = 0
  ## Loop to length-1 and access index i and i+1
  ## in the loop.
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            sum = sum + 1
    return sum


print(count_hi("h"))