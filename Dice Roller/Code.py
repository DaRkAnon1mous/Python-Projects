from tkinter import *
from random import *

# Dice unicode characters dictionary
Dice = {
    0: '🎲',
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}

App = Tk()
App.title("Dice Roller")

# First dice character to show when the app starts
die = Label(App, text=Dice[0], font=('Times', 100), foreground='black')
die.grid(row=0, column=0, padx=25, pady=5)


# Choose number from 1-6 randomly and display it
def roll():
    i = randint(1, 6)
    msg = Label(App, text=Dice[i], font=('Times', 100), foreground='black')
    msg.grid(row=0, column=0, padx=25, pady=5)


# Roll button
rollB = Button(App, text='Roll', command=roll, relief='raised')
rollB.grid(row=1, column=0)

App.mainloop()
