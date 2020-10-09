import random
import time

x = " "

SpecialCharacters = ["!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","=","<","=",">","?","@","[","]","^","_"]
EligibleWords = ["ZION","OVERSEER","WASTELAND","UTOBITHA","SCAB","CAESER","SORROWS","HUBOLOGY", "WORMFACE", "FINK", "GREENSKIN", "SLAGS"]

ActualWord = random.choice(EligibleWords)

WordsList = []

for i in range(11):
    RandomWord = random.choice(EligibleWords)
    WordsList.append(RandomWord)
    EligibleWords.remove(RandomWord)

RandomNumber1 = random.randint(15,30)
RandomNumber2 = random.randint(15,30)
RandomNumber3 = random.randint(15,30)
RandomNumber4 = random.randint(15,30)
RandomNumber5 = random.randint(15,30)
RandomNumber6 = random.randint(15,30)
RandomNumber7 = random.randint(15,30)
RandomNumber8 = random.randint(15,30)
RandomNumber9 = random.randint(15,30)
RandomNumber10 = random.randint(15,30)

for i in range(RandomNumber1):
    RandomCharacter = random.choice(SpecialCharacters)
    print(RandomCharacter, end = "")
print(WordsList[1], end = "")

for i in range(RandomNumber2):
    RandomCharacter2 = random.choice(SpecialCharacters)
    print(RandomCharacter2, end = "")
print(WordsList[2], end = "")
Total1 = RandomNumber1 + RandomNumber2 + len(WordsList[1]) + len(WordsList[2])

while Total1 < 80:
    FillerCharacters = random.choice(SpecialCharacters)
    print(FillerCharacters, end="")
    Total1 = Total1 + 1

print("")

for i in range(RandomNumber3):
    RandomCharacter3 = random.choice(SpecialCharacters)
    print(RandomCharacter3, end = "")
print(WordsList[3], end = "")

for i in range(RandomNumber4):
    RandomCharacter4 = random.choice(SpecialCharacters)
    print(RandomCharacter4, end = "")
print(WordsList[4], end = "")
Total2 = RandomNumber3 + RandomNumber4 + len(WordsList[3]) + len(WordsList[4])

while Total2 < 80:
    FillerCharacters2 = random.choice(SpecialCharacters)
    print(FillerCharacters2, end = "")
    Total2 = Total2 + 1

print("")

for i in range(RandomNumber5):
    RandomCharacter5 = random.choice(SpecialCharacters)
    print(RandomCharacter5, end = "")
print(WordsList[5], end = "")

for i in range(RandomNumber6):
    RandomCharacter6 = random.choice(SpecialCharacters)
    print(RandomCharacter6, end = "")
print(WordsList[6], end = "")
Total3 = RandomNumber5 + RandomNumber6 + len(WordsList[5]) + len(WordsList[6])

while Total3 < 80:
    FillerCharacters3 = random.choice(SpecialCharacters)
    print(FillerCharacters3, end="")
    Total3 = Total3 + 1

print("")

for i in range(RandomNumber7):
    RandomCharacter7 = random.choice(SpecialCharacters)
    print(RandomCharacter7, end = "")
print(WordsList[7], end = "")

for i in range(RandomNumber8):
    RandomCharacter8 = random.choice(SpecialCharacters)
    print(RandomCharacter8, end = "")
print(WordsList[8], end = "")
Total4 = RandomNumber7 + RandomNumber8 + len(WordsList[7]) + len(WordsList[8])

while Total4 < 80:
    FillerCharacters4 = random.choice(SpecialCharacters)
    print(FillerCharacters4, end="")
    Total4 = Total4 + 1

print("")

for i in range(RandomNumber9):
    RandomCharacter9 = random.choice(SpecialCharacters)
    print(RandomCharacter9, end = "")
print(WordsList[9], end = "")

for i in range(RandomNumber10):
    RandomCharacter10 = random.choice(SpecialCharacters)
    print(RandomCharacter10, end = "")
print(WordsList[10], end = "")
Total5 = RandomNumber9 + RandomNumber10 + len(WordsList[9]) + len(WordsList[10])

while Total5 < 80:
    FillerCharacters = random.choice(SpecialCharacters)
    print(FillerCharacters, end="")
    Total5 = Total5 + 1

print("")

CapitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
errorcount = 4

print("")
print("Welcome to ROBCO Industries (TM) Termlink")

while True:
    Count = 0
    print("")
    print("Attempts Remaining:", errorcount)
    UserChoice = input("Password Required: ")


    for i in UserChoice:
        if i not in CapitalLetters:
            print("You have to use capital letters!")
        if i in ActualWord:
            Count = Count + 1
    print("Likeness = ", Count)

    if UserChoice == ActualWord:
        print("")
        print("You did it!")
        break

    else:
        errorcount -= 1
        print("Entry denied")

        if errorcount == 0:
            print("You have been locked out")
            time.sleep(random.choice(range(5,20)))

            errorcount = 4

