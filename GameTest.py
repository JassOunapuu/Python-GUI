import random as r
from random import randint

hp = 0
coins = 0
damage = 0

# Parameetrite näitamine

def printParameters():
    print("")
    print("Sul on {0} elu, {1} luumurd(u) ja {2} money.".format(hp, damage, coins))

def printHp():
    print("")
    print("Sul on", hp, "elu.")

def printCoins():
    print("")
    print("Sul on", coins, "money.")

def printDamage():
    print("")
    print("Sul on", damage, "luumurd(u).")


# Kaupmehega kohtumine

def meetShop():
    global hp
    global damage
    global coins

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("")
        print("Sul pole raha, mine muretse juurde")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["Saatana sarv", "Kalevipoja nui", "Kivi (Saab visata)", "Ragulka", "Lestakala"]
    weaponRarities = ["Roostes", "Haruldane", "Legendaarne"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12
    
    print("")
    print("Teel kohtasite kaupmeest!")
    printParameters()

    if input("Kas tahad midagi osta või lahkuda? (O/L): ").upper() == "O":
        print("")
        print("1) Üks HP -", oneHpCost, "money;")
        print("2) Kolm HP -", threeHpCost, "money;")
        print("3) {0} {1} - {2} money".format(weaponRarity, weapon, weaponCost))
        global lopop
        global loop
        global lop

        choice = input("Mida tahad osta: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
                salvestamine()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
                salvestamine()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
                salvestamine()
        else:
            print("")
            print("Ma ei müü seda.")     
    elif input("Kas tahad mängust lahkuda? (jah/ei)").lower() == "jah":
        print("Tsau")
        salvestamine()
        loop = 0
        lop = 0
        
    
# Vastased/koletised, nende atribuudid ja nendega kohtumine

def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Kanged mehed Turjamaalt", "Härjapõlvlane", "Kratt", "Küla joodik", "Lumivalguke", "Saatana käsilane"]

    monster = r.choice(monsters)
    print("")
    print("Sa kohtasid vastast - {0}, Tal on {1} level, {2} elu ja {3} luumurd(u).".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        print("")
        choice = input("Mida sa teed ründa/jookse (R/J): ").lower()

        if choice == "r":
            monsterHp -= damage
            print("")
            print("Sa ründasid vastast ja tal on alles", monsterHp, "elu.")
        elif choice == "j":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("")
                print("Sul õnnestus lahinguväljalt põgeneda!")
                break
            else:
                print("")
                print("Vastane oli liiga tugev ja jõudis sulle järele...")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("")
            print("Vastane ründas ja te kaotasite", monsterDmg, "elu.")
            print("Teil on alles", hp, "elu.")
        
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl*2
        coins += loot
        print("")
        print("Teil õnnestus Vastane võita, mille eest saite", loot, "money.")
        printCoins()


# Mängu alustamine ja loopimine

def initGame(initHp, initCoins, initDamage):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDamage
    print("")
    print("Tere tulemast, siit algab sinu seiklus!")
    printParameters()

def gameLoop():
    situation = r.randint(0, 10)

    if situation == 0:
        meetShop()
    elif situation >= 8:
        meetMonster()
    else:
        input("Kõnnid mööda tänavat...")





# Mängu salvestamine ja laadimine  

def salvestamine():
    print("Mäng salvestati")
    with open('save.txt', 'w') as f:
         f.write(f"{hp} ")
         f.write(f"{coins} ")
         f.write(f"{damage} ")

def laadimine():
    with open(f"save.txt", "r")as f:
         for rida in f:
            a = rida.split(" ")
            hp = a[0]
            coins = a[1]
            damage = a[2]
            initGame(hp, coins, damage)




# Menüü printimine ja valikute tegemine

lopop = 1
loop = 1
while loop == 1:
    while lopop == 1:
        if int(coins) >= 100:
            print("tubli! sa võitsid!")
        print (30 * "-" , "MENÜÜ" , 30 * "-")
        print ("[1] Uus mäng")
        print ("[2] Lae mäng")
        print ("[3] Credits")
        print ("[4] Välju mängust")
        print (67 * "-")
        valik = int(input("valik [1-5]: "))
        lopop = 0
    if valik==1:
        print ("Tere tulemast uude mängu!")
        loop = 0
        initGame(randint(3, 6),randint(4, 8),randint(1, 3))
        lopop = 0
        lop = 1
        while lop == 1:
            gameLoop()

            if hp <= 0:
                if input("Kas tahad menüüsse tagasi minna? (jah/ei): ").lower() == "jah":
                    lopop = 1
                    loop = 1
                    lop = 0
                else:
                    lop = 0


    elif valik==2:
        print ("Laadisid mängu")
        laadimine()
        lopop = 0
        loop = 1
        lop = 1
    elif valik==3:
        print("")
        print ("Martin Pettai, Jass Õunapuu, Artjom Vinogradov")
        print("")
    elif valik==4:
        loop = 0
        exit()
    else:
        print("Vale valik, oled kindel, et vajutasid õiget klahvi?")
