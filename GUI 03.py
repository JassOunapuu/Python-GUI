# Jass Õunapuu
#  14.03.2022
#    IT-21


from tkinter import *

# akna seaded
aken = Tk()
aken.title('Tkinter Ülesanne 03')
aken.configure(background='black')
aken. geometry("") 
aken.resizable(0, 0)

# tekst
Label(aken, text="Nimi: Jass Õunapuu", foreground="red", background="black", pady=10, padx=30, font="Tahoma 16 bold italic", wraplength=aken.winfo_width(), justify=LEFT).pack()
Label(aken, text="Rühm: IT21", foreground="red", background="black", pady=10, padx=30, font="Tahoma 16 bold italic", wraplength=aken.winfo_width(), justify=LEFT).pack()
Label(aken, text="2016", foreground="red", background="black", pady=10, padx=30, font="Tahoma 16 bold italic", wraplength=aken.winfo_width(), justify=LEFT).pack()


aken.mainloop()
