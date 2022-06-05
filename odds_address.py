def arithmetic_sequence_sum(a, r, n):
    s,i=0,1
    while i<=n:
        s += a+r*(i-1)*i
        i+=1
    return s       


if __name__ == "__main__":
    arithmetic_sequence_sum(3, 2, 20)
