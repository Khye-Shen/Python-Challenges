
import random

color = raw_input("what's your favorite color")
place = raw_input("what's your favorite place")
animal = raw_input("what's your favorite animal")

special = ["#", "$", "&", "!", "%", "@"]

choice = random.choice([color, place, animal])

special_choice = random.choice(special)

password = choice + special_choice

print(password)