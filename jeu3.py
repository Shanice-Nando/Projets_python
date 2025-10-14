import random
from collections import Counter

mots = '''pomme banane cérise raisin ananas papaye citron lemon pastéque fraise mandarine mangue '''
mots = mots.split(' ')
mot = random.choice(mots)
if __name__ == '__main__':
    print("Devinez le mot! Astuce : le mot est le nom d'un fruit.")
    for i in mot:
        print("_", end=' ')
        print()
        jeu = True
        lettresuppose = ''
        essai = len(mot) + 2
        correct = 0
        drapeau = 0
        try:
            while (essai != 0) and drapeau == 0:
                print()
                essai -= 1
                try:
                    supposition = str(input("Entrer une lettre: "))
                except:
                    print("Entrer seulement une lettre!")
                    continue
                if not supposition.isalpha():
                    print("Entrer seulement une lettre.")
                    continue
                elif supposition in lettresuppose:
                    print("Vous avez déjà deviné une lettre")
                    continue

                if supposition in mot:
                    k = mot.count(supposition)
                    for _ in range(k):
                        lettresuppose += supposition
                        for char in mot:
                            if char in lettresuppose and (Counter(lettresuppose) != Counter(mot)):
                                print(char, end=' ')
                                correct += 1
                            elif Counter(lettresuppose) == Counter(mot):
                                print("Le mot est: ", end=' ')
                                print(mot)
                                drapeau = 1
                                print("Félicitations,vous avez gagné!")
                                break
                            break
                        else:
                            print("_", end=' ')
                            if essai <= 0 and Counter(lettresuppose) != Counter(mot):
                                print()
                                print("Vous avez perdeu! Essayez encore..")
                                print("le mot était{}".format(mot))
        except KeyboardInterrupt:
            print()
            print("Bye! Essayez encore.")
            exit()
