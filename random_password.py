import random
import os
from time import sleep


# List of all the characters

characters = [
              "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "@", "_", "-", "*", "!", "?"
              ]

password = []

# The function will choose a random charcter in the list above and add it to the password variable

def generate(lenght):
    for i in range(lenght):
        password.extend(random.choice(characters))
    print ("".join(str(i) for i in password))


os.system("cls")

# Handling every error possible

while True:
    try:
        lenght = int(input("Lenght of the password : "))
    except ValueError:
        print("\nPlease enter a valid number.")
        sleep(2)
        os.system("cls")
    else:
        if lenght <= 0:
            print("\nPlease choose a higher number.")
            sleep(2)
            os.system("cls")
        elif lenght > 30:
            print("\nPlease choose a lower number.")
            sleep(2)
            os.system("cls")
        else:
            break
            

sleep(0.5)
print("")
generate(lenght)
sleep(1)
print("\nYou can copy it now.")
sleep(10)       # Give enough time for the user to copy the password before the program ends
os.system("exit")
