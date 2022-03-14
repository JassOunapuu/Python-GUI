# Jass Õunapuu
#    IT-21
#  14.03.2022

import turtle
import random


#akna seaded
aken = turtle.Screen()
aken.setup(300,300)


# viisnurk
def viisnurk(v):
    t = turtle.Turtle()
    for x in range(0,5):
        t.forward(100)
        t.left(144)
        t.color(v)
    return viisnurk
viisnurk("red")
    
    


# kolmnurk
def kolmnurk(pikkus):
    t = turtle.Turtle()
    for x in range(0,3):
        t.forward(pikkus)
        t.left(120)
    return kolmnurk

kolmnurk(100)




