

end = int(input('What number would you like it to go up to? '))

x = 0

y = 1

z = 1

while (x < end):
    x = z + y
    y = x
    z = y

    print(x) 