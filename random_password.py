import random

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "@", "_", "-", "*", "!", "?"]
password = []

def generate(lenght):
    for i in range(lenght):
        password.extend(random.choice(characters))
    print ("".join(str(i) for i in password))

lenght = int(input("Longueur du mot de passe : "))

generate(lenght)
