a = [int(x) for x in input("Enter your ISBN Code: ")]
totalsum = 0

for x in range(9):
    totalsum = totalsum + (a[x] * (10-x))

ans = totalsum%11

if 11 - ans == a[9]:
    print("Valid ISBN.")
else:
    print("Invalid ISBN.")