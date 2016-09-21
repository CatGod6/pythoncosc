from tkinter import *

#Define the GUI APPLICATION

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

window = Tk()
window.geometry("400x200")

my_app = App(window)
my_app.master.title("I made a window")
my_app.mainloop()
