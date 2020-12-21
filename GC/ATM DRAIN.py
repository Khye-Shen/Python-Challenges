balance = 500


while True:
    withdraw = raw_input('Would you like to withdraw money? (y/n) ')

    if withdraw == 'y':

        print('You have $' + str(balance) + ' in your bank account')

        amount = int(input('How much money would you like to withdraw? '))

        if amount%5 != 0:
            print('ERROR! Not a multiple of 5')

        elif amount + 0.5 > balance:
            print('Insufficient balance!')

        else:
            balance = balance - (amount + 0.5)
            print('You have withdrawed $' + str(amount))

    if withdraw == "n":

        break

