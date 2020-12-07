brackets = ["(", ")", "[", "]", "{", "}"]

bracketcount = 0

while True:

    try:
        string = raw_input("Enter a string:")

        for i in string:
            if i in brackets:
                bracketcount = bracketcount + 1

        if bracketcount == 0:
            print("there are no brackets")

        else:
            bracketcount = bracketcount%2
            if bracketcount == 1:
                print("Error! Number of brackets aren't equal")
            else:
                break
    except ValueError:
        print("Error! Not a string")