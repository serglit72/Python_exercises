def count_sheep(n):
    s = " sheep..."
    obj = [str(i) for i in range(1,n+1)]
    return s.join(obj)+s

def count_sheeps(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

print (count_sheep(4))