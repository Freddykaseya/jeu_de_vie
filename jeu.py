import random
gamer1_name = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tentrez votre nom : ")
gamer2_name = "ordinateur"
life_gamer1 = 15
life_gamer2 = 15
print("\t\t\t\t\t\t\t\t\t\t\t\t\tvoici vos outils de combat et leurs cout:")
print("\t\t\t\t\t\t\t\t\t\t\t\t\tarme = 5 vies")
print("\t\t\t\t\t\t\t\t\t\t\t\t\tepée = 2  vie" )
print("\t\t\t\t\t\t\t\t\t\t\t\t\tbouclier = 2 chance")
print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t{gamer1_name} votre adversaire est {gamer2_name}")
def gamer1(option):
   global life_gamer2 
   life_gamer2 = 15
   life_gamer2 -= option
   print(f"vie de l'ordinateur = {life_gamer2}")
   return 

def gamer2():
    global life_gamer1
    life_gamer1 = 15
    number = random.randint(3,7)
    life_gamer1 -= number
    print(f"vie de  {gamer1_name} =  {life_gamer1}")
    return life_gamer1
def start_game():  
    while(life_gamer1>0 and life_gamer2>0):
        print(" 1 = arme , 2 = épee , 3 = bouclier ")
        outil = int(input("entrez votre choix : "))
        if outil == 1:
            gamer1(5)
            gamer2() 
        elif(outil == 2): 
            gamer1(3)
            gamer2()   
        elif(outil == 3 ):
            bouclier = 2
            if(bouclier < 3):
                print("plus de bouclier :")
                gamer1(0)
                gamer2()
            else:
                continue
        else:
            print("fin")
start_game()
        



   





