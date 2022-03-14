# Jass Õunapuu
#    IT-21
#  14.03.2022

import turtle
import random

aken = turtle.Screen()
aken.setup(300,300)
aken.title("Harjutus 01")

colors = ('red', 'blue', 'orange', 'green')
turn = 0
spikes = 8
size = 10
r = 10

for i in range(spikes):
    kk = turtle.Turtle()
    kk.left(turn)
    kk.forward(100)
    kk.color(random.choice(colors))
    turn += 45
    #kk.penup()
    #kk.forward(100)
    #kk.pendown()
    #kk.circle(r)
    
turtle.exitionclick()