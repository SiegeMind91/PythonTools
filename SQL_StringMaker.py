#!/usr/bin/python3
"""SQL WWID String Maker"""
from tkinter import *
from tkinter import ttk

class StringMaker:
    def __init__(self, master):
        master.title('StringMaker')
        master.resizeable(False, False) #We don't want this to be resizable
        master.configure(background = '#7EAAAA') #Changes the background color to be greyish blue 

        #Changes the background of the elements to greyish blue
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#7EAAAA')
        self.style.configure('TButton', background = '#7EAAAA')
        self.style.configure('TLabel', background = '#7EAAAA', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        #Header Frame creation
        self.frame_header = ttk.Frame(master) #Remember not to inline pack() when creating a variable, 
        self.frame_header.pack() # it will destroy the id value and replace with 'Nothing'

        #Header children creation
        self.logo = PhotoImage(file = 'tour_logo.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Desert to Sea Feedback Form', style = 'Header.TLabel').grid(row = 0, column = 1)
        #We're using a little Python magic here, long strings can be passed to the text property as lists
        ttk.Label(self.frame_header, wraplength = 300, text = ('We\'re glad you chose Explore California for your recent adventure'
                                                               'Please tell us what you thought about the \'Desert to Sea\' tour')).grid(row = 1, column = 1)


def SQL_String(self, string):
    wwids = string.split()


def main():
    root = Tk()
    strMaker = StringMaker(root)
    root.mainloop()

if __name__ == '__main__': main()
