import random



list = []

for i in range(50):
    list.append(random.randint(1,100))



print("Minimum:", min(list))


print("Maximum:", max(list))


print("Mean Average:", sum(list) / len(list))