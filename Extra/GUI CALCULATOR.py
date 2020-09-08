import tkinter

window = tkinter.Tk()
window.wm_title("Miles / Kilometers")
Unit_Number = ""


def evaluate(event):
    if Unit_Number == "Miles":
        try:
            entry = int(Myentry.get())
            kilometer = entry * 1.60934
            result1.configure(text="Kilometer is: " + str(kilometer))
        except ValueError:
            result1.configure(text="Please enter valid value in miles")
            result2.configure(text="")

    elif Unit_Number == "Kilometers":
        try:
            entry = int(Myentry.get())
            mile = entry * 0.621371
            result1.configure(text="Miles is: " + str(mile))
        except ValueError:
            result1.configure(text="Please enter valid value in kilometers")
            result2.configure(text="")

    else:
        result1.configure(text="Please select a unit!")


def calcStyle():
    global Unit_Number
    Unit_Number = unit.get()
    print(unit.get())


MyTitle = tkinter.Label(window, text="Miles / Kilometers")
MyTitle.pack()

Myentry = tkinter.Entry(window)
Myentry.bind("<Return>", evaluate)
Myentry.pack()

result1 = tkinter.Label(window, text="1. Choose a unit")
result1.pack()

result2 = tkinter.Label(window, text="2. Enter a number and press<enter>")
result2.pack()

unit = tkinter.StringVar()
tkinter.Radiobutton(window, text="Miles", variable=unit, value="Miles", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Kilometers", variable=unit, value="Kilometers", command=calcStyle).pack()

window.mainloop()