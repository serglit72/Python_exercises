#my solution
# def double_char(strg):
#     str1 = strg
#     strg2 = ""
#     for indx in range(len(str1)):
#         old = str1[indx]
#         new = old*2
#         strg2=strg2+new
#     return(strg2)

# optimal solution
def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result

print(double_char('The'))