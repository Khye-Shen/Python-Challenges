nice = 0


def check1(string):
    vowels =0
    for char in string:
        if char in "aeiouAEIOU":
           vowels = vowels+1
    return vowels
while True:
    try:
        string = input("Enter a string:")
        break
    except ValueError:
        print("Incorrect Value")

a = check1(string)
if a > 2:
    nice = nice + 1


def check2(string):
    x = 0
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            x = 1
    return x
b = check2(string)
if b == 1:
    nice = nice + 1


def check3(string):
    y = 0
    for i in range(len(string)-1):
        if string[i] + string [i+1] == 'ab' :
            y = 1
        elif string[i] + string [i+1] == 'cd' :
            y = 1
        elif string[i] + string [i+1] == 'pq' :
            y = y +1
        elif string[i] + string [i+1] == 'ab' :
            y = y + 1
        else:
            y = 2
    return y
c = check3(string)
if c == 2:
    nice = nice + 1


if nice == 3:
    print("this string is nice")
else:
    print("This string is naughty")