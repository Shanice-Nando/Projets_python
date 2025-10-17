import time
def compte_a_rebours(i):
    while i:
        mins,secs = divmod(i,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        i -= 1
    print("C'est bon!")
i = input("Entrer la durée du compte á rebours: ")
compte_a_rebours(int(i))