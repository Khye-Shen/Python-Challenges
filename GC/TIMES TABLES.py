x = int(input('Which times table would you like to display? '))
y = int(input('Which number is your end multiplier? '))
z = 1

for i in range(y):
    print(x*z)
    z += 1