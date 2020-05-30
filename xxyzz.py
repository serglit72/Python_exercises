def xyz_there(str):
    if len(str) != 0:
        for i in range(len(str)):
            if (str[i:i+3] == "xyz"):
                if ((str[i-1] or str[i+4]) != "."):
                    return True
    return False

print(xyz_there('1xyz.xyz2.xyz'))