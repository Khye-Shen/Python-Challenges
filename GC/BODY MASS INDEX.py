

height = float(input('What is your height in metres? '))

mass = float(input('What is your mass in kg? '))

bmi = mass / height ** 2

print('Your BMI is' + str(bmi))

if bmi < 18.5:
    print('UNDERWEIGHT')

if 18.5 <= bmi < 25:
    print('NORMAL WEIGHT')

if 25.0 <= bmi < 30.0:
    print('OVERWEIGHT')

if 30 <= bmi:
    print('OBESITY')

