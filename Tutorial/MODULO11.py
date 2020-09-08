
number_to_check = [1,2,3,4]

multiplier = [5,4,3,2]

checksum = 3

total_sum = 0

for i in range(len(number_to_check)):

    total_sum += number_to_check[i] * multiplier [i]


remainder = 11 - (total_sum % 11)

if checksum == remainder:
    print("pass")

else:
    print("error")