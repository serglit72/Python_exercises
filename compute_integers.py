# '5p11t290eoir8hqpr7' is given. Compute all integers but 99 is 99 and not 9+9

def compute_int(sntr):
    if len(sntr) != 0:
        integ = []
        digs = "0"
        for i in sntr:
            if i.isnumeric():
                digs += i
            elif i.isalpha():
                integ.append(int(digs))
                integ.append(0)
                digs = "0"
    integ.append(int(digs))
    summ = 0
    for y in range(len(integ)):
        summ += int(integ[y])
    return (summ)

print(compute_int('y1p22t10k0eoi090'))