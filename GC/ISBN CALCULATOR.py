numbers = []
ISBN = input('Enter the ISBN: ')

for i in range(len(ISBN)):
    if ISBN[i] != '-':
        numbers.append(ISBN[i])

for i in range(len(numbers)):
    if i%2 == 0 or i == 0:
        numbers [i] = int(numbers[i]) * 1

    else:
        numbers[i] = int(numbers[i]) * 3

total = 0

for i in range(12):
    total = total + numbers[i]

if total%10 == 0:
    checkdigit = 0

else:
    checkdigit = 10-(total%10)

print(checkdigit)