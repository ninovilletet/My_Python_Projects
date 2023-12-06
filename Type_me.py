from time import sleep

word = "Test n°1 : Result ?"
sleep(5)

for char in word:
    print(char, end='', flush=True)
    sleep(0.01)
