# Jass Õunapuu
#  15.03.2022
#    IT-21

import math
from tkinter import *
import tkinter.ttk

#akna seaded
aken = Tk()
aken.title('Nupud')
aken.geometry("300x200")

#sildid
silt = Label(aken, text="Vali käibemaks:")
silt.grid(row=1, column=0)
silt1 = Label(aken, text="Hind käibemaksuta:")
silt1.grid(row=0, column=0)
silt2 = Label(aken, text="käibemaks:")
silt2.grid(row=4, column=0)
silt3 = Label(aken, text="Hind käibemaksuga:")
silt3.grid(row=5, column=0)



#valikukast
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=1)
valikukast.grid(row=1, column= 1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=2)
valikukast.grid(row=2, column= 1)


#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

def arvuta():
    vari = var.get()
    sis = sisestus.get()
    if vari == 1:
        arv = round(float(sis)*0.09,2)
    else:
        arv = round(float(sis)*0.2,2)
        
        
        
        
    kmaks = float(arv) + float(sis)
    silt2.config(text=arv)
    silt3.config(text=kmaks)


#nupud
nupp1 = Button(aken, text="Arvuta", width=10, command=arvuta)
nupp1.grid(row=6, column=1)
silt2 =Label(aken, text=0.00)
silt2.grid(row=4, column=1)
silt3 =Label(aken, text=0.00)
silt3.grid(row=5, column=1)

# joon
silt = Label(aken, text="____________________________________________________________")
silt.grid(row=3, columnspan=2)

aken.mainloop()