import random
import turtle

direction = ['left', 'right']

pirate = turtle.Turtle()


for i in range(10):
    choice = random.choice(direction)
    if choice == 'left':
        angle = random.randint(1, 500)
        pirate.left(angle)

    if choice == 'right':
        angle = random.randint(1, 500)
        pirate.right(angle)

    pirate.forward(100)