# Jass Õunapuu
#  22.03.2022
#    IT-21


from tkinter import *

#akna seaded
aken = Tk()
aken.title('Joonistamine')
aken.geometry("800x400")


#lõuendi loomine
louend = Canvas(aken, width=800, height=500)
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

pilt1 = PhotoImage(file="pilt07.gif")
louend.create_image(400, 0, anchor=NW, image=pilt1)




aken.mainloop()