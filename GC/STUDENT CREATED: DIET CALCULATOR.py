calories = 0
foodlist = []

age = int(input('Enter your age: '))
if age <= 10:
    caloriesneeded = 1800

if age > 10 and age <= 20:
    caloriesneeded = 2500

if age > 20 and age <= 30:
    caloriesneeded = 2300

if age > 30 and age <= 40:
    caloriesneeded = 2300

if age > 40 and age <= 50:
    caloriesneeded = 2200

if age > 50:
    caloriesneeded = 2100

while True:
    food = raw_input('Enter the name of the food: ')
    if food == 'end day':
        break
    else:
        foodlist.append(food)
    calories = calories + int(input('Enter the number of calories: '))

    print('Total calories consumed:' + str(calories))
    print('You have eaten', foodlist)
    if caloriesneeded > calories:
        print('You need to consume', (caloriesneeded - calories), 'more calories.')

    if caloriesneeded < calories:
        print('You need to reduce intake by', (calories - caloriesneeded), 'calories.')

    if caloriesneeded == calories:
        print('You are eating healthy!')