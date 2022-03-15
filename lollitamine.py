# Jass Õunapuu
#  15.03.2022
#    IT-21

from tkinter import *
from random import *

#akna seaded
aken = Tk()
aken.title('Nupud')
aken.geometry("1000x1000")

arv1 = randint(10,999)
arv2 = randint(10,999)

#funktsioonid
def liigu():
    arv1 = randint(10,999)
    arv2 = randint(10,999)
    nupp1 = Button(aken, text="Vajuta mind", width=10, command=liigu)
    nupp1.place(x=arv1, y=arv2)

    
liigu()
    
    #nupud
#nupp1 = Button(aken, text="Vajuta mind", width=10, command=liigu)
#nupp1.place(x=arv1, y=arv2)





aken.mainloop()
    
    
    
    
    
    
    
    
    