
from tkinter import *
from datetime import datetime

App = Tk()
App.title("Age Calculator")
App['background'] = 'white'
App.geometry('300x300')

# Enter Your DOB
lbl = Label(App, text='Enter Your DOB', background='white', foreground='black')
lbl.grid(row=0, column=3, columnspan=2)

# Date Label & Entry
dateL = Label(App, text='Date:', background='white', foreground='black')
dateE = Entry(App, background='white', foreground='black', width=2)

# Month Label & Entry
monL = Label(App, text='Month:', background='white', foreground='black')
monE = Entry(App, background='white', foreground='black', width=2)

# Year Label & Entry
yrL = Label(App, text='Year:', background='white', foreground='black')
yrE = Entry(App, background='white', foreground='black', width=4)


dateL.grid(row=1, rowspan=1, column=1)
dateE.grid(row=1, rowspan=1, column=2)
monL.grid(row=1, rowspan=1, column=3)
monE.grid(row=1, rowspan=1, column=4)
yrL.grid(row=1, rowspan=1, column=5)
yrE.grid(row=1, rowspan=1, column=6)


# Finding Total days and creating its Label
def find_days():
    year = int(yrE.get())
    month = int(monE.get())
    day = int(dateE.get())
    dob = datetime(year=year, month=month, day=day)

    time_now = datetime.now()
    time_dif = time_now - dob
    msg = Label(App, text='You lived ' + str(time_dif.days) + ' days!', background='white',
                foreground='black')
    msg.grid(row=3, column=0, columnspan=3)


# Finding Total seconds and creating its Label
def find_sec():
    year = int(yrE.get())
    month = int(monE.get())
    day = int(dateE.get())
    dob = datetime(year=year, month=month, day=day)

    time_now = datetime.now()
    time_dif = time_now - dob
    msg = Label(App, text='You lived ' + str(time_dif.total_seconds()) + ' seconds!', background='white',
                foreground='black')
    msg.grid(row=6, column=3, columnspan=6)


# Buttons for finding total days & seconds
daysB = Button(App, text='Total days', command=find_days, background='white', foreground='black')
scndB = Button(App, text='Total seconds', command=find_sec, background='white', foreground='black')
# Placing the buttons
daysB.grid(row=5, column=1, padx=5, pady=5, columnspan=3)
scndB.grid(row=5, column=4, padx=5, pady=5, columnspan=3)

App.mainloop()

