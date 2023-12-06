
#JEU DU PENDU (HANGMAN HAME)

import os
import time
import sys


#CLEAR

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def write(sentence):
    for char in sentence:
        print(char, end='', flush=True)
        time.sleep(0.01)

       
# PARAMETRES PAR DEFAUT

right_guess = 0
fault = 0
word = " "
clear()
time.sleep(0.5)


#VERIFIER LES FAUTES

def hangman_check():
    if fault == 0:
        write("   |‾‾‾‾‾‾‾‾")
        write("   |        ")
        write("   |        ")
        write("   |        ")
        write("   |        ")
        write(" ------")
    if fault == 1:
        write("   |‾‾‾‾‾‾‾‾|")
        write("   |         ")
        write("   |         ")
        write("   |         ")
        write("   |         ")
        write(" ------")
    if fault == 2:
        write("   |‾‾‾‾‾‾‾‾|")
        write("   |        O")
        write("   |         ")
        write("   |         ")
        write("   |         ")
        write(" ------")
    if fault == 3:
        write("   |‾‾‾‾‾‾‾‾|")
        write("   |        O")
        write("   |        |")
        write("   |         ")
        write("   |         ")
        write(" ------")
    if fault == 4:
        write("   |‾‾‾‾‾‾‾‾|")
        write("   |        O")
        write("   |       /|")
        write("   |         ")
        write("   |         ")
        write(" ------")
    if fault == 5:
        write("   |‾‾‾‾‾‾‾‾|")
        write("   |        O")
        write("   |       /|\\")
        write("   |         ")
        write("   |         ")
        write(" ------")
    if fault == 6:
        write("   |‾‾‾‾‾‾‾‾|")
        write("   |        O")
        write("   |       /|\\")
        write("   |       / ")
        write("   |         ")
        write(" ------")
    if fault == 7:
        write("   |‾‾‾‾‾‾‾‾|")
        write("   |        O")
        write("   |       /|\\")
        write("   |       / \\")
        write("   |         ")
        write(" ------")


#TUTO ET REGLES

def tutorial():
    clear()
    write("Bienvenue dans le jeu du pendu.")
    time.sleep(2)
    write("\nVoici les règles du jeu : ")
    time.sleep(2)
    write("\nCe jeu se joue à 2 joueurs. Un joueur choisi un mot et l'autre doit le deviner en proposant des lettres.")
    time.sleep(6)
    write("\nLe joueur qui doit deviner le mot n'a le droit qu'à 7 fautes.")
    time.sleep(4)
    write("\nBonne chance !")
    time.sleep(2)
    clear()


#TUTO ?

while True:
    tuto = int(input("Tutoriel et règles ? \n(OUI = 1  |  NON = 2)   "))
    if tuto == 1:
       tutorial()
       break
    elif tuto == 2:
        break
    else:
        write("Choisi entre 1 et 2 !")
        time.sleep(1)
        clear()


#VICTOIRE

def win():
    clear()
    time.sleep(0.5)
    hangman_check()
    write("Tu as gagné !")
    time.sleep(1)
    write("\nTu as deviné le mot '{}'".format(word))
    time.sleep(3)
    sys.exit()


#DEFAITE

def defaite():
    clear()
    time.sleep(0.5)
    hangman_check()
    time.sleep(1.5)
    write("Tu as perdu.")
    time.sleep(1)
    write("\nLe mot était '{}' .".format(word))
    time.sleep(3)
    sys.exit()


#CHOIX DU MOT

clear()
while True:
    word = input("Le joueur 1 choisi un mot :  ")
    time.sleep(0.1)
    if word.isalpha():
        clear()
        write("Ton mot est valide.")
        time.sleep(2)
        clear()
        time.sleep(1)
        break
    else:
        write("Tu n'as pas le droit de mettre des chiffres !")
        time.sleep(1.5)
        clear()
        time.sleep(1)


#DEBUT DU JEU

word = word.lower()
word_set = set(word)
hidden_word = ["_"] * len(word)
hangman_check()
time.sleep(2)
clear()


#JEU :

#PROPOSITION D'UNE LETTRE

while fault != 7:
    write(" ".join(hidden_word))
    letter = input("\nPropose une lettre : ").lower()

    if letter in word_set:

#LA LETTRE EST DANS LE MOT

        write("\nLa lettre '{}' est dans le mot.".format(letter))
        for i, char in enumerate(word):
            if char == letter:
                hidden_word[i] = letter
                right_guess += 1
        if right_guess == len(word_set):
            win()
            break
        time.sleep(2)
        clear()

#LA LETRRE N'EST PAS DANS LE MOT

    else:
        fault += 1
        write("\nLa lettre '{}' n'est pas dans le mot.".format(letter))
        time.sleep(2)
        clear()
        hangman_check()
        time.sleep(2)
        clear()


defaite()

#FIN

sys.exit()
