import time

siblings = int(input('How many siblings do you have? '))

turn = int(input('How much time would you like each turn to be in seconds? '))
time.sleep(0.5)




for x in range(86400/turn):
    time.sleep(turn)
    print('Ring!')
    time.sleep(0.5)
    print('Time for you to stop!')