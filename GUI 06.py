# Jass Õunapuu
#  22.03.2022
#    IT-21

import tkinter as tk
from tkinter import *
import time
from PIL import ImageTk, Image

#akna seaded
aken = Tk()
aken.title('Joonistamine')
aken.geometry("500x500")


#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()


#kujund

louend.create_rectangle(0, 0, 350, 100, fill="#02b2f2", outline="#ffffff")
louend.create_rectangle(0, 100, 350, 120, fill="#ffffff", outline="#000000")
louend.create_rectangle(0, 160, 350, 120, fill="#000000", outline="#ffffff")
louend.create_rectangle(0, 180, 350, 100, outline="#ffffff")
louend.create_rectangle(0, 180, 350, 280, fill="#02b2f2", outline="#ffffff")


#sildid

silt = Label(aken, text="Botswana lipp")
silt.place(x=150, y=280)


#pilt
pilt1 = "botswana.jpg"
pilt = ImageTk.PhotoImage(Image.open(pilt1))
paneel = tk.Label(aken, image = pilt)

paneel.pack(side = "bottom", fill = "both", expand = "yes")



aken.mainloop()