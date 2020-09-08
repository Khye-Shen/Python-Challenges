from random import randint
import time



class Player:
    def __init__(self, name):
        self.kills = 0
        self.name = name
        self.health = 50
        self.max_health = 50
        self.attack = 10
        self.defence = 10
        self.weaponName = "Fist"
        self.life = True


    def xp_check(self):
        if self.kills == 5 or self.kills == 10 or self.kills == 15 or self.kills == 20 or self.kills == 25:
            print("You earned a skill point!")
            time.sleep(2)
            print("What would you like to add the skill point too?")
            print("1. Attack", "    ", "Attack lv currently: ", self.attack)
            print("2. Defence", "    ", "Defence lv currently: ", self.defence)
            print("3. Health", "    ", "Max Health currently: ", self.max_health)
            skill = ""
            while skill not in ("1", "2", "3"):
                skill = raw_input("enter: 1/2/3  -")
                if skill == "1":
                    self.attack += 20
                elif skill == "2":
                    self.defence += 20
                elif skill == "3":
                    self.max_health += 40
                else:
                    print("Please re-enter")
            self.health = self.max_health

    def print_info(self):
        print("Name:       ", self.name)
        print("health:     ", self.health)
        print("attack:     ", self.attack)
        print("defence:     ", self.defence)
        print("weapon:      ", self.weaponName)

class Enemy:
    def __init__(self):

        name = ["Random angry slime", "Ben the Bat",  "Orc", "Goblin", "Zombie", "Skeleton", "Dark Dwarf Miner", "Minotaurus", "Undead Knight","Phantom"]
        weapon = ["Fists", "Stick (+5 atk)", "Razor Teeth (+15 atk)", "Brick (+25 atk)", "Pole (+30 atk)", "knife (+50 atk)","Hammer (+60 atk)", "Sharp knife (+70 atk)","Dagger (+75 atk)", "Katana(+100 atk)"]

        self.difficulty_check()

        self.name = name[randint(0, self.difficulty)]
        self.health = 25 * randint(1, self.difficulty)
        self.max_health = 25 * randint(1, self.difficulty)
        self.attack = 5 * randint(1, self.difficulty)
        self.defence = 5 * randint(1, self.difficulty)
        self.weaponName = weapon[randint(0, self.difficulty)]
        self.life = True

    def difficulty_check(self):
        self.difficulty = 1
        if Hero.kills == 5 or Hero.kills == 10 or Hero.kills == 15 or Hero.kills == 20:
            if self.difficulty < 10:
                self.difficulty += (2 * (Hero.kills / 5))


    def print_info(self):
        print("Name:", self.name)
        print("health:", self.health)
        print("attack:", self.attack)
        print("defence:", self.defence)
        print("weapon:", self.weaponName)



player = (raw_input("Name your character: "))
Hero = Player(player)


def weapon_drop():
    chance = randint(1, 4)
    if chance == 2:
        print("The enemy has dropped his weapon", Enemy_Create.weaponName)
        ans = int(input("Do you want to pick it up? Yes(1) / No(2)"))

        if ans == 1:
            Hero.weaponName = Enemy_Create.weaponName

def Pwp():

    if Hero.weaponName == "Stick (+5 atk)":
        Pwp_dmg = 5

    elif Hero.weaponName == "Razor Teeth (+15 atk)":
        Pwp_dmg = 15

    elif Hero.weaponName == "Brick (+25 atk)":
        Pwp_dmg = 25

    elif Hero.weaponName == "Pole (+30 atk)":
        Pwp_dmg = 30

    elif Hero.weaponName == "knife (+50 atk)":
        Pwp_dmg = 50

    elif Hero.weaponName == "Hammer (+60 atk)":
        Pwp_dmg = 60

    elif Hero.weaponName == "Sharp knife (+70 atk)":
        Pwp_dmg = 70

    elif Hero.weaponName == "Dagger (+75 atk)":
        Pwp_dmg = 75

    elif Hero.weaponName == "Katana(+100 atk)":
        Pwp_dmg = 100

def Ewp():

    if Enemy_Create.weaponName == "Stick (+5 atk)":
        Ewp_dmg = 5

    elif Enemy_Create.weaponName == "Razor Teeth (+15 atk)":
        Ewp_dmg = 15

    elif Enemy_Create.weaponName == "Brick (+25 atk)":
        Ewp_dmg = 25

    elif Enemy_Create.weaponName == "Pole (+30 atk)":
        Ewp_dmg = 30

    elif Enemy_Create.weaponName == "knife (+50 atk)":
        Ewp_dmg = 50

    elif Enemy_Create.weaponName == "Hammer (+60 atk)":
        Ewp_dmg = 60

    elif Enemy_Create.weaponName == "Sharp knife (+70 atk)":
        Ewp_dmg = 70

    elif Enemy_Create.weaponName == "Dagger (+75 atk)":
        Ewp_dmg = 75

    elif Enemy_Create.weaponName == "Katana(+100 atk)":
        Ewp_dmg = 100


while Hero.life == True:

    Hero.xp_check()

    Enemy_Create = Enemy()

    Enemy_Create.difficulty_check()

    print("A", Enemy_Create.name, "appears!")

    time.sleep(2)


    Action_P = 2
    EAction_P = 2

    while Hero.life == True and Enemy_Create.life == True:

        print("")
        print("Enemy's Stats")

        time.sleep(1)

        Enemy_Create.print_info()

        time.sleep(2)

        print("")
        print("Your Stats")

        time.sleep(1)

        Hero.print_info()
        print("")

        time.sleep(3)

        e_atk = 0
        e_def = 0
        e_cons = 0
        p_atk = 0
        p_def = 0
        p_cons = 0


        for i in range(EAction_P):
            enemy_choice = 0
            enemy_choice = randint(1, 3)

            if enemy_choice == 1:
                e_atk += 1

            elif enemy_choice == 2:
                e_def += 1

            elif enemy_choice == 3:
                e_cons += 1


        print("Action Points:", Action_P)
        print("Do you want to attack(1) / block(2) / conserve(3) ?")


        for j in range(Action_P):

                choice = int(input("enter: 1/2/3 "))

                if choice == 1:
                    p_atk += 1

                elif choice == 2:
                    p_def += 1

                elif choice == 3:
                    p_cons += 1

        #weapon damage
        Pwp_dmg = 0
        Ewp_dmg = 0
        Pwp()
        Ewp()


        if p_atk > e_def:
            for i in range(p_atk - e_def):
                Enemy_Create.health = Enemy_Create.health - ((Hero.attack + Pwp_dmg) - (Enemy_Create.defence / 10))
        else:
            Action_P = 2 + p_cons


        if e_atk > e_def:
            for i in range(e_atk - p_def):
                Hero.health = Hero.health - ((Enemy_Create.attack + Ewp_dmg) - (Hero.defence / 10))
        else:
            EAction_P = 2 + e_cons


        print("")
        print(Enemy_Create.name, "used", e_atk, "attack point", e_def, "defense point", e_cons, "conserve points")

        if Hero.health <= 0:
            Hero.life = False

            print("You are dead, GAME OVER!")

            print("You got", Hero.kills, "kills")

            break

        elif Enemy_Create.health <= 0:

            print(Enemy_Create.name, "has been killed")
            print("")

            weapon_drop()

            Enemy_Create.life = False
            Hero.kills += 1

        time.sleep(3)


