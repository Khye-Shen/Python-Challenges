

def denarytoBCD(n):
    nlist = ([int(i) for i in str(n)])

    BCDlist = []

    for j in nlist:


        BCD = bin(j)[2:].zfill(4)

        BCDlist.append(BCD)

    print(BCDlist)


n = int(input("Enter Number:"))
denarytoBCD(n)