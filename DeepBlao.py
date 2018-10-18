import sys, time
from tkinter import *

from time import sleep

root = Tk()

root.config(borderwidth=5)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(0,0)

WB=[2]*16
BB=[2]*16

Wframe = Frame(root, bg="green")
Wframe.grid(column=0, row=0, sticky=N+S+E+W)

Bframe = Frame(root, bg="green")
Bframe.grid(column=0, row=1, sticky=N+S+E+W)

WLabs = []
BLabs = []
for cup in range(0,16):
    WLabs.append(StringVar())
    BLabs.append(StringVar())

Wedges = {}
Wcups = {}

for cup in range(0,16):

    if cup >= 8:
        Wcol = 15 - cup
        Wrow = 0
    else:
        Wcol = cup
        Wrow = 1
    
    Wframe.grid_rowconfigure(Wrow, weight=1)
    Wframe.grid_columnconfigure(Wcol, weight=1) 
    Wedges[cup] = Frame(Wframe, width = 30, height = 30, borderwidth=3, relief=SUNKEN)
    Wedges[cup].grid(row=Wrow, column=Wcol, sticky=N+S+E+W)
    Wedges[cup].grid_columnconfigure(0, weight=1,minsize=30)
    Wedges[cup].grid_rowconfigure(0, weight=1,minsize=30)
    Wcups[cup] = Button(Wedges[cup], bg="white", textvariable = WLabs[cup], command = lambda cup=cup: Wmove(cup, "R"))

    Wcups[cup].grid(column=0, row=0, sticky=N+S+E+W)

Bedges = {}
Bcups = {}

Brow = 0
Bcol = 0
for cup in range(0,16):

    if cup >= 8:
        Bcol = 15 - cup
        Brow = 1
    else:
        Bcol = cup
        Brow = 0

    Bframe.grid_rowconfigure(Brow, weight=1)
    Bframe.grid_columnconfigure(Bcol, weight=1)    
    Bedges[cup] = Frame(Bframe, width = 30, height = 30, borderwidth=3, relief=SUNKEN)
    Bedges[cup].grid(row=Brow, column=Bcol, sticky=N+S+E+W)
    Bedges[cup].grid_columnconfigure(0, weight=1,minsize=30)
    Bedges[cup].grid_rowconfigure(0, weight=1,minsize=30)
    Bcups[cup] = Button(Bedges[cup], bg="black", textvariable = BLabs[cup], foreground = "white", command = lambda cup=cup: Bmove(cup, "R"))
    Bcups[cup].grid(column=0, row=0, sticky=N+S+E+W)


def board(WB,BB):
    for cup in range(0,16):
        WLabs[cup].set(WB[cup])
        BLabs[cup].set(BB[cup])
        root.update_idletasks()
        
def Wmove(cuppick, direction):
    currcup = cuppick
    while WB[currcup] > 1:
        startbeans = WB[currcup]
        WB[currcup] = 0
        for bean in range(0,startbeans):
            currcup = currcup + 1
            if currcup == 16:
                currcup = 0
            WB[currcup] = WB[currcup] + 1
        board(WB,BB)
        sleep(1)


def Bmove(cuppick, direction):
    currcup = cuppick
    while BB[currcup] > 1:
        startbeans = BB[currcup]
        BB[currcup] = 0
        for bean in range(0,startbeans):
            currcup = currcup + 1
            if currcup == 16:
                currcup = 0
            BB[currcup] = BB[currcup] + 1
        board(WB,BB)
        sleep(1)

Movebutton = Button(root, bg="green", command=lambda: Wmove(1, "R"))
Movebutton.grid(column=0, row=2, sticky=N+S+E+W)

board(WB,BB)

root.mainloop()
