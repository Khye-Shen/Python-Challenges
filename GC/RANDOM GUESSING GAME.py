import random

print('I will pick a number from 1 to 100 and you will guess')

noguesses = 0
guess = 0
number = random.randint(1,100)

while guess != number:

    noguesses +=  1

    guess = int(input('Guess the number: '))
    if guess > number:
        print('Smaller!')
    if guess < number:
        print('Larger')

print('You took ' + str(noguesses) + ' tries')