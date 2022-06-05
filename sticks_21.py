def make_move(sticks):
    total = 21
    
    while total > 0:
        total -= sticks
        
    return total
    
    

print(make_move(3))
print(make_move(1))
print(make_move(3))
print(make_move(2))


