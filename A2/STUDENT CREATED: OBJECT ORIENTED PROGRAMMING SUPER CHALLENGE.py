from random import randint
import threading
import time



class Character:

    def __init__(self):
        self.attack = 5
        self.defence = 5
        self.health = 100


    def print_basics(self):
        print("attack:     ",self.attack)
        print("defence     ",self.defence)
        print("health:     ",self.health)


    def class_getter(self):

        if choice == 1:
            self.__class = "Kickboxer"

        elif choice == 2:
            self.__class = "Boxer"

        elif choice == 3:
            self.__class = "Sumowrestler"

        return self.__class

    def print_me(self):
        self.class_getter()
        print("type:       ", self.class_getter())
        self.print_basics()




class kickboxer(Character):
    def __init__(self):
        Character.__init__(self)

    def setter(self):
        self.__class = "KickBoxer"
        self.attack = self.attack * (randint(1,5))
        self.defence = self.defence * (randint(0,2))
        self.health = self.health * (randint(1,6))


    class move:

        def action():
            print("*kick*")



class boxer(Character):
    def __init__(self):
        Character.__init__(self)


    def setter(self):
        self.__class = "Boxer"
        self.attack = self.attack * (randint(1,4))
        self.defence = self.defence * (randint(0,3))
        self.health = self.health * (randint(1,7))


    class move:

        def action():
            print("*punch*")



class sumowrestler(Character):
    def __init__(self):
        Character.__init__(self)

    def setter(self):
        self.__class = "Sumowrestler"
        self.attack = self.attack * (randint(1,2))
        self.defence = self.defence * (randint(0,10))
        self.health = self.health * (randint(1,10))


    class move:

        def action():
            print("*slap*")

#Selection


choice = int(input("Which character do you want? / Kickboxer (1) / Boxer (2) / Sumowrestler (3) "))
if choice == 1:
    Player = kickboxer()
    Player.setter()

elif choice == 2:
    Player = boxer()
    Player.setter()

elif choice == 3:
    Player = sumowrestler()
    Player.setter()


print("Your Stats:")

Player.print_me()

time.sleep(3)


#bot character

choice = randint(1, 3)

if choice == 1:
    Bot = kickboxer()
    Bot.setter()

elif choice == 2:
    Bot = boxer()
    Bot.setter()

elif choice == 3:
    Bot = sumowrestler()
    Bot.setter()

print("")
print("Bot Stat:")

Bot.print_me()

time.sleep(3)

#battle


def player_atk():

    while True:

        raw_input("Enter to Attack!")

        Bot.health = Bot.health - (Player.attack - (Bot.defence / 10))

        print("Bot has",Bot.health ,"hp left")

        if Player.health <= 0 or Bot.health <= 0:
            break

    if Player.health <= 0:
        print("The bot defeated you, YOU LOST")

    elif Bot.health <= 0:
        print("You defeated the bot, YOU WIN")

def bot_atk():

    while True:

        time.sleep(0.2)

        Player.health = Player.health - (Bot.attack - (Player.defence / 10))

        print("You have", Player.health, "hp left")

        if Player.health <= 0 or Bot.health <= 0:
            break

    if Player.health <= 0:
        print("The bot defeated you, YOU LOST")

    elif Bot.health <= 0:
        print("You defeated the bot, YOU WIN")


print("")

raw_input("Press enter to start:")

print("FIGHT!")

thread1 = threading.Thread(target=bot_atk)
thread1.start()

thread2 = threading.Thread(target=player_atk)
thread2.start()


