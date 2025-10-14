import random
name = input("Quel est votre nom ?")
print("Bonne chance !", name)
mots =['mouton',"quiz" ,"arc-en-ciel","demon-slayer","bonjour","python","entomological",
        "sociability","code","information","programme"]
mot = random.choice(mots)
print("Dévinez les lettres pour constituer le mot choisi.")

suppositions = ''
essais = 12
while essais > 0:
    echec = 0
    for char in mot:
        if char in suppositions:
            print(char,end=" ")
        else:
           print("_")
           echec += 1

    if echec == 0 :
        print("Vous avez gagné!")
        print("Le mot est : " , mot)
        break

    print()
    supposition = input("Dévinez une lettre :")
    suppositions += supposition
    if supposition not in mot :
       essais -= 1
       print("Faux")
       print("Vous n'avez plus que ",+essais,"suppositions restantes.")
       if essais == 0:
          print("Vous avez perdu!!!!")



