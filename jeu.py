import random
gamer1_name = input("entrez votre nom ")
gamer2_name = "ordinateur"
life_gamer1 = 100
life_gamer2 = 100
outils = ["arme","epée","bouclier"]
print("voici vos outils de combat :")
print("arme = 5, epée = 2 , bouclier")
print(f"{gamer1_name} votre adversaire est {gamer2_name}")
def gamer1(option):
   life_gamer2 = 100
   life_gamer2 -= option
   print(f"life game2  = {life_gamer2}" )
   return 

def gamer2():
    life_gamer1 = 100
    number = random.randint(3,7)
    life_gamer1 -= number
    print(f"voici le vie de l'ordinateur = {life_gamer1}")
    return life_gamer1

while(life_gamer1>0 and life_gamer2>0):
    def round_gamer1():
        print(" 1 = arme , 2 = épee , 3 = bouclier ")
        outil = int(input("entrez votre choix : "))
        while outil == 2 and outil == 5:
            if outil == 1:
                gamer1(5)
                print("joeur 2 ")
                gamer2() 
            elif(outil == 2): 
                 gamer1(3)
                 print("joeur 2 ")
                 gamer2()   
            elif(outil == 3 ):
                bouclier = 2
                if(bouclier == 3):
                    print("plus de bouclier :")
                    gamer2()
        return
round_gamer1()



   





