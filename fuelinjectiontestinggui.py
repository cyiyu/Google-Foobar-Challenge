from Tkinter import *

number = 0

window = Tk()
window.title("Yeet")
window.geometry('500x200')

label = Label(window, text="Number: {}".format(number))
label.grid(column=0, row=0)

entryLabel = Label(window, text="Enter a number: ")
entryLabel.grid(column=3, row=0)
entry = Entry(window)
entry.grid(column=4, row=0)

moves = 0

labelMoves = Label(window, text="Moves: {}".format(moves))
labelMoves.grid(column=1, row=0)


def enterNumber():
    global number
    global moves
    moves = 0
    number = int(entry.get())
    labelMoves.config(text="Moves: {}".format(moves))
    label.config(text="Number: {}".format(number))


def updateMoves():
    global moves
    moves += 1
    labelMoves.config(text="Moves: {}".format(moves))


def addOne():
    global number
    number += 1
    label.config(text="Number: {}".format(number))
    updateMoves()


def removeOne():
    global number
    number -= 1
    label.config(text="Number: {}".format(number))
    updateMoves()


def divTwo():
    global number
    number /= 2
    label.config(text="Number: {}".format(number))
    updateMoves()


button = Button(window, text="Add 1", command=addOne)
button.grid(column=1, row=2)
button = Button(window, text="Remove 1", command=removeOne)
button.grid(column=2, row=2)
button = Button(window, text="Divide 2", command=divTwo)
button.grid(column=3, row=2)
button = Button(window, text="Enter", command=enterNumber)
button.grid(column=5, row=0)

window.mainloop()
