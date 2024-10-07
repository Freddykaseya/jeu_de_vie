import random

# Inscription de membre du jeu 
gamer1_name = input("\tentrez votre nom : ")
gamer2_name = "ordinateur"
print(f"\t{gamer1_name} votre adversaire est {gamer2_name} ")
print("vous avez chacun 15 vie ")

def attack():
    print("\tchoisissez votre attaque:")
    print("\t1. arme = 5 vies")
    print("\t2. epée = 2  vies" )
    print("\t3. bouclier = 2 chances")

# cette fonction marque le debut du jeu 
#    
def start_game(): 
    life_gamer1 = 15
    life_gamer2 = 15 
    protection = 2

    print(f"{gamer1_name} et {gamer2_name} bienvenue dans le jeu de rôle")

# la boucle qui lance le jeu 
    try :
        while life_gamer1 > 0 and life_gamer2 > 0 :

            attack_gamer2 = random.randint(3,7) 

            attack()
            try:
                tools = int(input("entrez votre choix : "))
            except ValueError:
                print("veuillez choisir un chiifre allant de 1 à 3 en suivant les outils ci-dessous :")
                continue
            if tools == 1:
                life_gamer2 -=5
                print(f"gamer {gamer2_name}= {life_gamer2}")
                life_gamer1 -= attack_gamer2
                print(f"gamer {gamer1_name} votre vie = {life_gamer1}")
           
            elif tools == 2: 
                life_gamer2 -= 3
                print(f"gamer {gamer2_name}= {life_gamer2}")
                life_gamer1 -= attack_gamer2
                print(f"gamer {gamer1_name} votre vie = {life_gamer1}")
            elif tools == 3 :
                if(protection < 3):
                    protection -= 1
                    print(f"vous avez utilisé le bouclier il vous reste : {protection}")
                elif protection == 0:
                    life_gamer1 -= attack_gamer2
                    print(f"{gamer1_name} vous n'avez plus de bouclier et vous avez perdue {attack_gamer2}")
                    print(f"gamer {gamer2_name}= {life_gamer2}")
                    print(f"gamer {gamer1_name} votre vie = {life_gamer1}")
                else:
                    print("vous n'avez plus de bouclier")
                    life_gamer1 -= attack_gamer2
                print(f"gamer {gamer2_name} votre vie = {life_gamer2}")
                print(f"gamer {gamer1_name} votre vie = {life_gamer1}")
            else : 
                print("choix invalide")
            print("****************************************************")
        if life_gamer1 <= 0 :
            print(f"GAME OVER et le gamer {gamer2_name} gagne avec = {life_gamer2} vie")
            
        else:
            print(f"Bravooooo, {gamer1_name}  avec {life_gamer1} contre {life_gamer2} de vie")
    

    finally:
        print("************************")
        

    #  Fin du jeu 
start_game()
        



   





