import tkinter
import random
window = tkinter.Tk()


def RandomNumber():
    Choose_Name = ["James", "John", "Mark", "Rick"]
    MyRandom = random.choice(Choose_Name)
    name_chosen.configure(text="Name Chosen: " + str(MyRandom))



MyTitle = tkinter.Label(window, text="Random Number Generator",font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="OK", command=RandomNumber)
MyButton.pack()

name_chosen = tkinter.Label(window, font="Helvetica 16 bold")
name_chosen.pack()

window.mainloop()