#Example program to illustrate my issue with dynamic buttons.

from tkinter import *

class my_app(Frame):
    """Basic Frame"""
    def __init__(self, master):
        """Init the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.Create_Widgets()

    def Create_Widgets(self):
        for i in range(1, 11):
            self.newmessage = Button(self, text= "Button ID: %d" % i, anchor=W,
                                     command = lambda i=i: self.access(i))
            self.newmessage.config(height = 3, width = 100)
            self.newmessage.grid(column = 0, row = i, sticky = NW)

    def access(self, b_id): #This is one of the areas where I need help. I want this to return the number of the button clicked.
        self.b_id = b_id
        print(self.b_id) #Print Button ID

#Root Stuff


root = Tk()
root.title("Tkinter Dynamics")
root.geometry("500x500")
app = my_app(root)

root.mainloop()
