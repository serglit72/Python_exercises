def is_in_middle(sequence):
    middle = len(sequence) // 2
    indx = sequence.index("b")
    if (middle - sequence.index("a")) >1:
        print("False")
        return False
    else: 
        print("True")
        return True

if __name__ == "__main__":
    sequence = "AAabcBBB"
    is_in_middle(sequence)