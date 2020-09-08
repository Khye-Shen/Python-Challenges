
list = [5, 7, 1, 9, 3]

def sum(numbers):

    total = 0
    for i in numbers:
        total += i
    return total


def product(numbers):

    total = 1

    for i in numbers:
        total = total * i

    return total


print(sum(list))

print(product(list))