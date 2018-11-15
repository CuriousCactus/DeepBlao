import sys, time
from tkinter import *

from time import sleep

# initialise tk
root = Tk()									

# set up window
root.config(borderwidth=5)					
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(0,0)

# intial bean configuration
WB=[2]*16									
BB=[2]*16

# frame for white beans
Wframe = Frame(root, bg="green")			
Wframe.grid(column=0, row=0, sticky=N+S+E+W)

# frame for black beans
Bframe = Frame(root, bg="green")			
Bframe.grid(column=0, row=1, sticky=N+S+E+W)

# labels for bean cups
WLabs = []									
BLabs = []
for cup in range(0,16):
    WLabs.append(StringVar())
    BLabs.append(StringVar())

# frames for white bean cups
Wedges = {}
# buttons for white bean cups
Wcups = {}									

# set up white bean cups
for cup in range(0,16):						

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
	
	# bind left mouse click
	Wcups[cup].bind('<Button-1>', lambda event, cup=cup: Wmove(cup, 1))
	# bind right mouse click
	Wcups[cup].bind('<Button-3>', lambda event, cup=cup: Wmove(cup, -1))  
	Wcups[cup].grid(column=0, row=0, sticky=N+S+E+W)

# frames for black bean cups
Bedges = {}
# buttons for black bean cups
Bcups = {}									

# set up black bean cups
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
	if Brow == 0 and Bcol == 4:
		Bcups[cup] = Button(Bedges[cup], bg="grey", textvariable = BLabs[cup], foreground = "white")
	else:
		Bcups[cup] = Button(Bedges[cup], bg="black", textvariable = BLabs[cup], foreground = "white")
	Bcups[cup].bind('<Button-1>', lambda event, cup=cup: Bmove(cup, 1))   # bind left mouse click
	Bcups[cup].bind('<Button-3>', lambda event, cup=cup: Bmove(cup, -1))  # bind right mouse click
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
	# check move allowed
	while WB[curcup] > 1:								
		startbeans = WB[curcup]
		# pick up beans
		WB[curcup] = 0 									
		for bean in range(0,startbeans):
			# sow beans
			curcup = (curcup + curdir) % 16				
			WB[curcup] += 1
		# taking opponent's beans
		if curcup < 8 and WB[curcup] > 1 and BB[7-curcup]>0:
			# checking where to put them
			if curcup < 2 or (curdir == 1 and curcup < 6):		
				restartcup = 0
				curdir = 1
			else:
				restartcup = 7
				curdir = -1
			WB[restartcup] += BB[7-curcup]
			BB[7-curcup] = 0
			# starting from new position
			curcup = restartcup
			# so you can follow what's happening
			sleep(1)
		# updating board
		board(WB,BB)
		# so you can follow what's happening
		sleep(1)										


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
			sleep(1)
		board(WB,BB)
		sleep(1)

Movebutton = Button(root, bg="green", command=lambda: Wmove(1, 1))
Movebutton.grid(column=0, row=2, sticky=N+S+E+W)

board(WB,BB)

root.mainloop()
