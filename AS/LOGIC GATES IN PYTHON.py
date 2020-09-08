
def NAND (a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True


def AND(a, b):

    if NAND(a, b) == True:
        return False
    else:
        return True



def OR(a, b):

    if NAND(a, b) == True:
        if a == 0 and b == 0:
            return False
        else:
            return True
    else:
        return True


def XOR (a, b):

    if NAND(a, b) == 1:
        if a == 0 and b == 0:
            return False
        else:
            return True
    else:
        return False


def NOT(a):
    if (a == 0):
        return 1
    elif (a == 1):
        return 0



def NOR(a, b):

    if OR(a, b) == False:
        return True

    else:
        return False

print(AND(1,0))