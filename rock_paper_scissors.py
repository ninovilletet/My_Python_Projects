import random
import os
import time
import sys

def erase(n):
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


bot_score = 0
player_score = 0
os.system("cls")
print("Welcome to Rock, Paper, Scissors !")
time.sleep(2)
num_rounds = int(input("Number of rounds : "))
time.sleep(1)
os.system("cls")


# Starting game
for i in range(num_rounds):
    result = None
    player_choice = None
    bot_choice = None

# Bot

    bot = random.randint(1, 3)
    if bot == 1:
        bot_choice = "Rock"
    elif bot == 2:
        bot_choice = "Paper"
    elif bot == 3:
        bot_choice = "Scissors"


# Player

    print(str("Rock = 1   Paper = 2  Scissors = 3"))
    print("")
    time.sleep(1)
    while True:
        try:
            player = int(input("Choice : "))
            if player in (1, 2, 3):
                break
            else:
                print("Choose a number between 1, 2, 3 !")
                time.sleep(1.5)
                erase(2)
        except ValueError:
            print("Choose a digit !")
            time.sleep(1.5)
            erase(2)


    if player == 1:
        player_choice = "Rock"
    elif player == 2:
        player_choice = "Paper"
    elif player == 3:
        player_choice = "Scissors"
    time.sleep(1)
    print("")

# Tie

    if player == 1 and bot == 1:
        result = "Tie"
    elif player == 2 and bot == 2:
        result = "Tie"
    elif player == 3 and bot == 3:
        result = "Tie"

# Bot won

    elif bot == 1 and player == 3:
        result = "Bot won"
    elif bot == 2 and player == 1:
        result = "Bot won"
    elif bot == 3 and player == 2:
        result = "Bot won"
    
# Player won   
 
    elif player == 1 and bot == 3:
        result = "Player won"
    elif player == 2 and bot == 1:
        result = "Player won"
    elif player == 3 and bot == 2:
        result = "Player won"
    
# Changing score
    if result == "Player won":
        player_score += 1
    elif result == "Bot won":
        bot_score += 1
    else:
        pass
     

# End of the game
    score = str(player_score) + "  -  " + str(bot_score)
    print("Bot chose :", bot_choice, "and you chose :", player_choice)
    print("")
    time.sleep(2)
    print(result)
    time.sleep(2)
    print(score)
    time.sleep(2)
    os.system("cls")

time.sleep(5)
sys.exit()