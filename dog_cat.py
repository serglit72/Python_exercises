def cat_dog(str):
    c=0
    d=0
    for i in range(len(str)):
        if str[i:i+3] == "dog":
            d +=1
            print ("d = ",d)

        elif str[i:i+3] == "cat":
            c +=1
            print ("c = ",c)
    return d == c

print(cat_dog('catcatdigdog1doggy'))