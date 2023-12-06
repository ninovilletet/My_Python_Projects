import random
import time
import os

os.system("cls")
def play_game():
    num = random.randint(1, 10)
    print ("Un nombre aléatoire entre 1 et 10 a été choisi.")
    while True:
        try:
            guess = int(input("Entre ta proposition : "))
        except ValueError:
            print ("Entre un nombre !")
        else:
            if guess < num:
                print ("Ta proposition est trop basse.")
            elif guess > num:
                print ("Ta proposition est trop élevée.")
            else:
                print("Bravo ! Tu as trouvé la bonne réponse !")
                time.sleep(2)
                break


play_game()
