

import random
options = ["silent", "confess"]

while True:
    print("You have been caught for a crime, if you confess and your partner stays quiet, you will be released but your partner will be inprison for 20 years.\nIf you're both silent, you both only be inprison for a year.\nIf you both confess, you both will be inprison for 5 years.")

    a = raw_input("Do you want to sat silent or confess?")
    b = random.choice(options)

    if a == "silent" and b == "silent":
        print("You both are inprison for a year")

    elif a == "confess" and b == "silent":
        print("You're releassed, and your partner is inprison for 20 years")

    elif a == "silent" and b == "confess":
        print("You're inprison for 20 years, and your partner is released")

    elif a == "confess" and b == "confess":
        print("You both are inprison for 5 years")

    replay = raw_input("If you want to play again?")
    if replay in ["Yes", "yes", "y", "Y"]:
        for i in range(15):
            print(" ")
    else:
        break