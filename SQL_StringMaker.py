#!/usr/bin/python3
"""SQL WWID String Maker"""
from tkinter import *
from tkinter import ttk

class StringMaker:

    def __init__(self, master):
        master.title('StringMaker')
        #master.resizeable(False, False) #We don't want this to be resizable
        master.configure(background = '#7EAAAA') #Changes the background color to be greyish blue 

        # Changes the background of the elements to greyish blue
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#7EAAAA')
        self.style.configure('TButton', background = '#7EAAAA')
        self.style.configure('TLabel', background = '#7EAAAA', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        # Header Frame creation
        self.frame_header = ttk.Frame(master) #Remember not to inline pack() when creating a variable, 
        self.frame_header.pack() # it will destroy the id value and replace with 'Nothing'

        # Header children creation
        ttk.Label(self.frame_header, text = 'SQL String Maker', style = 'Header.TLabel').grid(row = 0, column = 1, padx=20)
        #We're using a little Python magic here, long strings can be passed to the text property as lists
        ttk.Label(self.frame_header, wraplength = 300, text = ('Paste in your line separated items and it will return '
                                                               'the list as a comma separated, single line of items')).grid(row = 1, column = 1, padx=20)
        
        # Content Frame creation
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        # Creating our entry text box that will take in the list
        self.entryText = Text(self.frame_content, height=15, width=30)
        self.entryText.grid(row = 2, column = 0, columnspan = 1, rowspan=1, padx=10)

        # Button Frame creation
        self.frame_button = ttk.Frame(master)
        self.frame_button.pack()

        button = Button(self.frame_button, text = 'Create String')
        button.pack()
        button.config(command = self.SQL_String)
        button.grid(padx = 10, pady=5)
         
    # Function for creating the new string
    def SQL_String(self):
        Lines = self.entryText.get('1.0', END).splitlines()
        counter = 0
        result = ""
        for line in Lines:
            if counter == 0:
                result = line
                counter += 1
            else:
                result = result + ', ' + line
        self.entryText.delete('1.0', END)
        self.entryText.insert('1.0', result)
        result = ""

def main():
    root = Tk()
    root.geometry("350x380")
    strMaker = StringMaker(root)
    root.mainloop()

if __name__ == '__main__': main()
