

def graycode(n):

    if n == 0:
        return ['']
    first_half = graycode(n - 1)
    second_half = first_half

    first_half = ['0' + i for i in first_half]
    second_half = ['1' + i for i in second_half[::-1]]

    return first_half + second_half


n = int(input('Enter the number of bits: '))
print(graycode(n))

