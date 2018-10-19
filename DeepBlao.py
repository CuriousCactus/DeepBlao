import sys, time
from tkinter import *

from time import sleep

root = Tk()									# initialise tk

root.config(borderwidth=5)					# set up window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(0,0)

WB=[2]*16									# intial bean configuration
BB=[2]*16

Wframe = Frame(root, bg="green")			# frame for white beans
Wframe.grid(column=0, row=0, sticky=N+S+E+W)

Bframe = Frame(root, bg="green")			# frame for black beans
Bframe.grid(column=0, row=1, sticky=N+S+E+W)

WLabs = []									# labels for bean cups
BLabs = []
for cup in range(0,16):
    WLabs.append(StringVar())
    BLabs.append(StringVar())

Wedges = {}									# frames for white bean cups
Wcups = {}									# buttons for white bean cups

for cup in range(0,16):						# set up white bean cups

	if cup >= 8:
		Wcol = cup - 8
		Wrow = 0
	else:
		Wcol = 7 - cup
		Wrow = 1
    
	Wframe.grid_rowconfigure(Wrow, weight=1)
	Wframe.grid_columnconfigure(Wcol, weight=1) 
	Wedges[cup] = Frame(Wframe, width = 30, height = 30, borderwidth=3, relief=SUNKEN)
	Wedges[cup].grid(row=Wrow, column=Wcol, sticky=N+S+E+W)
	Wedges[cup].grid_columnconfigure(0, weight=1,minsize=30)
	Wedges[cup].grid_rowconfigure(0, weight=1,minsize=30)
	if Wrow == 1 and Wcol == 3:
		Wcups[cup] = Button(Wedges[cup], bg="grey", textvariable = WLabs[cup], foreground = "white")
	else:
		Wcups[cup] = Button(Wedges[cup], bg="white", textvariable = WLabs[cup])
			
	def leftclick(event):
		Wmove(cup, 1)
	def rightclick(event):
		Wmove(cup, -1)
		
	Wcups[cup].bind('<Button-1>', leftclick)   # bind left mouse click ############# this doesn't currently work!!! #############
	Wcups[cup].bind('<Button-3>', rightclick)  # bind right mouse click
	Wcups[cup].pack()
	Wcups[cup].grid(column=0, row=0, sticky=N+S+E+W)

Bedges = {}									# frames for black bean cups
Bcups = {}									# buttons for black bean cups

for cup in range(0,16):						# set up black bean cups

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
    if Brow == 0 and Bcol == 4:
    	Bcups[cup] = Button(Bedges[cup], bg="grey", textvariable = BLabs[cup], foreground = "white", command = lambda cup=cup: Bmove(cup, 1))
    else:
    	Bcups[cup] = Button(Bedges[cup], bg="black", textvariable = BLabs[cup], foreground = "white", command = lambda cup=cup: Bmove(cup, 1))
    Bcups[cup].grid(column=0, row=0, sticky=N+S+E+W)


# to update board
def board(WB,BB):
    for cup in range(0,16):
        WLabs[cup].set(WB[cup])
        BLabs[cup].set(BB[cup])
        root.update_idletasks()
 
# to move white beans       
def Wmove(cuppick, direction):
	curcup = cuppick
	curdir = direction
	while WB[curcup] > 1:								# check move allowed
		startbeans = WB[curcup]
		WB[curcup] = 0 									# pick up beans
		for bean in range(0,startbeans):				
			curcup = (curcup + curdir) % 16				# sow beans
			WB[curcup] += 1
		if curcup < 8 and WB[curcup] > 1 and BB[7-curcup]>0:	# taking opponent's beans
			if curcup < 2 or (curdir == 1 and curcup < 6):		# checking where to put them
				restartcup = 0
				curdir = 1
			else:
				restartcup = 7
				curdir = -1
			WB[restartcup] += BB[7-curcup]
			BB[7-curcup] = 0
			curcup = restartcup							# starting from new position
		board(WB,BB) 									# updating board
		sleep(1)										# so you can follow what's happening


# to move black beans  
def Bmove(cuppick, direction):
	curcup = cuppick
	curdir = direction
	while BB[curcup] > 1:
		startbeans = BB[curcup]
		BB[curcup] = 0
		for bean in range(0,startbeans):
			curcup = (curcup + direction) % 16
			BB[curcup] += 1
		if curcup < 8 and BB[curcup] > 1 and WB[7-curcup]>0:		
			if curcup < 2 or (curdir == 1 and curcup < 6):
				restartcup = 0
				curdir = 1
			else:
				restartcup = 7
				curdir = -1
			BB[restartcup] += WB[7-curcup]
			WB[7-curcup] = 0
			curcup = restartcup
		board(WB,BB)
		sleep(1)

Movebutton = Button(root, bg="green", command=lambda: Wmove(1, 1))
Movebutton.grid(column=0, row=2, sticky=N+S+E+W)

board(WB,BB)

root.mainloop()
