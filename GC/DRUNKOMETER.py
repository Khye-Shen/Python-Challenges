
print('The phrase is: Fred fed Ted bread, and Ted fed Fred bread')

while True:

    x = raw_input('Type the phrase: ')
    if x != 'Fred fed Ted bread, and Ted fed Fred bread':
        print('You are very drunk')
        break


    if x == 'Fred fed Ted bread, and Ted fed Fred bread':
        print('You are okay!')
        break

