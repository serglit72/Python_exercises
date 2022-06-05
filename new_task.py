def sum_str_1(a, b):
    return str(int(a or 0) + int(b or 0))


def sum_str(a, b):
    if a == "" and b != "":
        s = int(b)
        return str(s)

    elif b == "" and a != "":
        s = int(a)
        return str(s)
    elif a == "" and b == "":
        return "0"
    else:
        s = str(int(a)+int(b))
        return s

if __name__ == "__main__":

    a = "-3"
    b = ''
    print(int(a))
    print(int(b or 0))
    # print(sum_str_1(a, b))