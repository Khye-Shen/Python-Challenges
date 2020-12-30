

Milo = ("Milo", "milo")
MiloValue = 5
Sprite = ("Sprite", "sprite")
SpriteValue = 4
Coke = ("Coke", "coke")
CokeValue = 3


print("VENDING MACHINE")

print("Milo - 5 coins")
print("Sprite - 4 coins")
print("Coke - 3 coins")

while True:
    Coins = int(input("Enter coins: "))

    Drink = raw_input("Enter a drink:")

    if Drink in Milo:
        if Coins < MiloValue:
            print("Not enough coins")
        else:
            Change = Coins - MiloValue
            print("Collect your Milo")
            if Change != 0:
                print("Collect your " + str(Change) + " coins")
            break

    if Drink in Sprite:
        if Coins < SpriteValue:
            print("Not enough coins")
        else:
            Change = Coins - SpriteValue
            print("Collect your Sprite")
            if Change != 0:
                print("Collect your " + str(Change) + " coins")
            break

    if Drink in Coke:
        if Coins < CokeValue:
            print("Not enough coins")
        else:
            Change = Coins - CokeValue
            print("Collect your Coke")
            if Change != 0:
                print("Collect your " + str(Change) + " coins")
            break
