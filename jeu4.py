import random
print("Les régles du jeu PIERRE-PAPIER-CISEAUX sont :\n"
      +"Pierre vs Papier -> Papier gagne \n"
      +"Papier vs Ciseaux -> Ciseaux gagne \n"
      +"Pierre vs Ciseaux -> Pierre gagne \n")
while True:
    print("OPTIONS: \n 1-Pierre \n 2-Papier \n 3-Ciseaux ")
    choix = int(input("Entrer votre choix: "))
    while choix > 3 or choix < 1:
        choix= int(input("Entrer un choix valide s'il vous plaît!"))
    if choix == 1:
            nom_choix = "Pierre"
    elif choix == 2:
            nom_choix = "Papier"
    else:
            nom_choix = "Ciseaux"
            print("Votre choix est: ",nom_choix)
            print("C'est le tour de la machine ")
    mach_choix = random.randint(1,3)
    if mach_choix == 1:
                mach_nom_choix = "Pierre"
    elif mach_choix== 2:
                mach_nom_choix ="Papier"
    else:
                mach_nom_choix = "Ciseaux"
                print("le choix de la machine est: ",mach_nom_choix)
                print(nom_choix ,"vs",mach_nom_choix)
    resultat= "choix vs mach_choix"
    if choix == mach_choix:
        resultat = "Match-NULL"
    elif (choix == 1 and mach_choix==2) or (mach_choix ==1 and choix==2):
       resultat= "Papier"
    elif (choix==1 and mach_choix==3) or (mach_choix==1 and choix ==3):
       resultat= "Pierre"
    elif (choix==2 and mach_choix==3) or (mach_choix==2 and choix==3):
       resultat= "Ciseaux"
    if resultat == "Match-NULL":
                        print("<==C'est un match null!==>")
    elif resultat == nom_choix:
                        print("Vous avez gagné!")
    else:
                        print("<==La machine a gagné!==>")
                        print("Voulez jouer encore? O/N")
    ans = input().lower()
    if ans == "n":
                            break
print("MERCI POUR CETTE PARTIE!")



