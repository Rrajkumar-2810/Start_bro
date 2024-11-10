from tkinter import *

root = Tk()
# To create a root Window using Tkinter
root.title("First Step")
root.geometry('425x300')

menu = Menu(root)
item = Menu(menu)
menu.add_cascade(label = 'File', menu = item)
item.add_command(label = 'New')
root.config(menu = menu)

lbl1 = Label(root, text = "Are you a Student?")
lbl1.grid()

#Button to chnage the text colour and the text upon clicking
txt1 = Entry(root, width=10)
txt1.grid(column=1, row=0)

def clicked1():
    lbl1.configure(text = "I just got Clicked")
btn1 = Button(root, text = "Click me", fg = "Red", command =clicked1)
btn1.grid(column=2, row=0)

def clicked2():
    lbl1.configure(text="How are you?")
btn2 = Button(root, text ="Well-Being", fg ="dark green", command =clicked2)
btn2.grid(column=3, row=0)

root.mainloop()
