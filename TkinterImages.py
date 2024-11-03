import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
root.title("Image Carousel")
root.geometry('1920x1080')

img1 = ImageTk.PhotoImage(Image.open("D:/PYVSCODE/Start_bro/Screenshot 1.png"))
img2 = ImageTk.PhotoImage(Image.open("D:/PYVSCODE/Start_bro/Screenshot 2.png"))
img3 = ImageTk.PhotoImage(Image.open("D:/PYVSCODE/Start_bro/Screenshot 3.png"))
l = Label()
l.pack()

x=1
def move():
    global x
    if x==4:
        x=1
    if x == 1:
        l.config(image= img1)
    elif x == 2:
        l.config(image= img2)
    elif x == 3:
        l.config(image= img3)
    x= x+1
    root.after(2000, move)

move()
root.mainloop()
