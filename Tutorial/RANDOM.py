
import random

mynumber = random.uniform(0.1, 9.9)



Choose_Name = ["James","John","Mark","Rick"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print(chosen)
    choice = raw_input("do you want to keep the name in the list? y/n")
    if choice in ["n"]:
        Choose_Name.remove(chosen)