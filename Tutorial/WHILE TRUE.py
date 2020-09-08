while True:
    love_status = raw_input('Is computer science the best subject? y/n')
    if love_status == "n" :
        print("wrong!!!")
    else:
        print("knew it!")
        break



number = 0 
while number < 14.5 or number > 20.5 :
    print("Please enter a number between 15 and 20")
    number = float(input("enter a number:"))