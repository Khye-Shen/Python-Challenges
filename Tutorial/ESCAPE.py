error_count = 0

while True:
    MyNumber = raw_input("Please enter a number: ")
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        error_count += 1
        print("Seriously, don't you read the instructions. \nI asked for a number...")

print(valid_number)
print("You made", error_count, "errors")