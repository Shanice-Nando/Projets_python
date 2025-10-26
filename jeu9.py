import random
num = random.randrange(1000,10000)
n = int(input("Dévinez les 4 numéros:"))
if (n==num):
    print("Bravo! Tu as déviné le numéro juste en un essai ! Tu es vraiment un génie!")
else:
    ctr=0
    while (n != num):
        ctr +=1
        count=0
        n= str(n)
        num=str(num)
        correct= ['X']*4
        for i in range (0,4):
            if (n[i]==num[i]):
                count +=1
                correct[i]= n[i]
            elif (count == 0):
             print("Aucun des nombre de votre saisie ne correspond.")
             n = int(input("Entrer votre prochain choix de numéros: "))
            else:
                continue
            print("Ce n'est pas tout à fait le nombre. Mais vous avez obtenu",count,"chiffre(s) correct(s)!")
            print ('\n')
            print('\n')
            n = int(input("Entrer votre prochain choix de numéros: "))
       
if n == num:
    ctr ==1 
    print ("Tu es devenu un GÉNIE!")
    print("Il ne t'as fallu que",ctr,"essais.")
        


            