print("This is a speed, distance, time calculator!")

print("")

x = raw_input("Which variable are you trying to find?")

if x == "speed":
    Distance = int(input("What is the distance?"))
    Time = int(input("What is the time?"))
    print(Distance/Time)

if x == "distance":
    Speed = int(input("What is the speed?"))
    Time = int(input("What is the time?"))
    print(Speed*Time)

if x == "time":
    Distance = int(input("What is the distance?"))
    Speed = int(input("What is the speed?"))
    print(Distance/Speed)