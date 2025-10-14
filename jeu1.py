import random

print ("Bienvenue! Le jeu est simple ,tu disposes de 7 chances" \
" pour deviner le nombre éxact choisit par l'ordinateur " \
"dans un intervalle que tu auras fixé au debut du jeu. C'est parti!")

min = int(input("Entrer une borne inférieure: "))
max = int (input("Entrer une borne supérieure: "))
print (f"Tu disposes de 7 chances pour trouver le nombre compris entre {min} et {max}. C'est parti!")

num= random.randint(min , max)
chance = 7
compteur_essai = 0

while compteur_essai < chance :
    compteur_essai += 1
    essai = int(input("Entrer votre nombre: "))
    if essai == num :
        print (f"Félicitations! Vous avez trouvé le nombre exact {num} en {compteur_essai} tentatives")
        break
    elif compteur_essai >= chance and essai != num :
        print(f" Dommage! Le nombre exact est {num}. Vous réussirez la prochaine fois.")
    elif essai > num :
        print(f"Trop haut! Rééssayez de nouveau!")
    elif essai < num :
        print(f"Trop bas! Rééssayez de nouveau!")
