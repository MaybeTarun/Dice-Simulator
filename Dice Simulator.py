import random
from tkinter import *

root = Tk()
root.title('Dice Simulator')
root.geometry("800x400")

l1 = Label(root, font=("times", 200))

def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()

def roll2():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1 = Button(root, text="Roll a Die", command = roll)
b1.place(x=300, y=0)
b2 = Button(root, text="Roll 2 Dice", command = roll2)
b2.place(x=400, y=0)

root.mainloop()