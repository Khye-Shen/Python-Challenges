

i = 0
for i in range(20):
    if (i+1)%3 == 0 and (i+1)%5 != 0:
        print('Fizz')

    if (i+1)%5 == 0 and (i+1)%3 != 0:
        print('Buzz')

    if (i+1)%3 == 0 and (i+1)%5 == 0:
        print('Fizzbuzz')

    if (i+1)%3 != 0 and (i+1)%5 != 0:
        print(i+1)