#Mäng
#Martin Pettai, Artjom Vinogradov, Jass Õunapuu
#IT21



#elden kalevipoeg


def print_menuu():    
    print (30 * "-" , "MENÜÜ" , 30 * "-")
    print ("[1] Uus mäng")
    print ("[2] Lae mäng")
    print ("[3] Vaata mängijat")
    print ("[4] Credits")
    print ("[5] Exit")
    print (67 * "-")
  
loop=True
  
while loop:   
    print_menuu()   
    valik = int(input("Enter your valik [1-5]: "))
     
    if valik==1:     
        print ("Tere tulemast uude mängu!")
        nimi = input("Sisestage nimi: ")
        loop = False
    elif valik==2:
        print(" ")
    elif valik==3:
        print(" ")
    elif valik==4:
        print(" ")        
    elif valik==5:
        print(" ")
        loop = False
    else:
        print("Vale valik, oled kindel et vajutasid õiget klahvi?")
    






from random import *

def calculate_heal(self, heal_amount):
    if (heal_amount + self.health > 100):
        self.health = 100
        print("{0} heals back to full health!".format(self.name.capitalize()))
    else:
        self.health += heal_amount
        print("{0} heals for {1}!".format(self.name.capitalize(), heal_amount))



def me():
    HP = 20
    ATK = 5
    DEF = 4
    print(f"{nimi}: ")
    print(f"Elud= {HP}")
    print(f"ATK= {ATK}")
    print(f"DEF= {DEF}")
me()
print("")




def rott():    
    kHP = randint(2, 13)
    kATK = randint(2, 10)
    kDEF = randint(0, 5)
    print(" ")
    if kHP > 10:
        print("Vastane: Tugev rott")
    else:
        print("Vastane: Rott")
    print(f"Elud= {kHP}")
    print(f"ATK= {kATK}")
    print(f"DEF= {kDEF}")





v = int(input("Kas tahad kakelda?\n 1. JAAA! \n 2. EI :( \n "))


if v == 1:
    rott()
    rott.kHP
else:
    print("u ar pussy")
    print("")








# menüü







'''
print("Mäng")

tehe=int(input('You want to play litle boy?\n 1) YES\n 2) NO\n'))

if tehe==1:
   print("Oh man Thats very nice")
   
elif tehe==2:
    print("Man I dont care you dont have a choise")
    
    
print('I will ask you a few questions and life of Kalevi Poeg will depend on the correct answer')

first=int(input('First question:3 boys from the village, want to fight with Kalevi Poeg, what are you going to do?\n 1)run away\n 2)fight back with a hug from the left\n 3)answer verbally\n'))

if first==1:
    print('you barely managed to escape but you pissed your pants')
    
elif first==2:
    print('You hit one with such force that he most likely died, and the others run away and you were left unharmed')
'''