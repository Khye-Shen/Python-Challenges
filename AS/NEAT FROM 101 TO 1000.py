
neat_list = []

for i in range(101, 1001):

    split = []
    denominator = 0

    split = [int(d) for d in str(i)]

    for j in (split):

        denominator += j

    if i % denominator == 0:

        neat_list.append(i)

print(neat_list)