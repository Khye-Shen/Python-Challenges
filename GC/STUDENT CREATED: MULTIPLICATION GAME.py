import random

score = 0

n = int(input("How many questions?: "))

for x in range(n):
    a = random.randint(1,12)
    b = random.randint(1,12)

    ans = a * b
    print("What is " + str(a) + " x " + str(b))

    userans = int(input("Answer: "))

    if ans == userans:
        print("Correct")
        score += 1
    else:
        print("Wrong")
print("\n\nYour final score is: " + str(score) + "/" + str(n))