from tkinter import *

window = Tk()
window.title("Here's a window")
window.geometry("250x100") #default window size

my_frame = Frame()
my_frame.pack()

label_text = Label(my_frame, text ="I've been framed!",
                   bg="blue", fg="Red", font="Arial")
label_text.pack(fill=X)

window.mainloop()
