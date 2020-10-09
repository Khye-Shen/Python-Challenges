import random
from random import randint

def IPV4():

    ip = "192.168."
    ip += ".".join(map(str, (random.randint(0, 255) for _ in range(2))))

    return ip


def IPV6():

    hex = "0 1 2 3 4 5 6 7 8 9 a b c d e f"
    hex = hex.split(" ")

    address = []

    all_uppercase = False

    for block in range(8):
        one = hex[randint(0, 15)]
        two = hex[randint(0, 15)]
        three = hex[randint(0, 15)]
        four = hex[randint(0, 15)]
        address.append(one)
        address.append(two)
        address.append(three)
        address.append(four)
        address.append(":")

    address.pop()
    address = "".join(address)

    if all_uppercase == True:
        return address.upper()
    else:
        return address

IPV4_list = []
IPV6_list = []

for i in range(1):

    print(IPV4())
    print(IPV6())