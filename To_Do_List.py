# TO-DO LIST

import os
import time
import sys
from colorama import Fore
import json


# DEFAULT SETTINGS

Fore.WHITE

options = [0, 1, 2, 3, 4, 5]

# USE THE PREVIOUS DATAS SAVED IN A JSON FILE

def load_tasks():
    try:
        with open("list_tasks.json", "r") as file:
            return json.load(file)
            
# IF THE FILE DOESN'T EXIST THEN CREATE A NEW ONE
    
    except FileNotFoundError:
        with open ("list_tasks.json", "w") as file:
            json.dump([], file)
        return []
    
# JUST IN CASE THE JSON FILE HAS A PROBLEM  

    except json.JSONDecodeError:
        write_red("Error decoding JSON file. The file might be corrupted.")
        return []


list_tasks = load_tasks()

task_name = ""


# EVERY ACTIONS

def save_tasks():
    global list_tasks
    with open("list_tasks.json", "w") as file:
        json.dump(list_tasks, file)



def sleep(seconds):
    time.sleep(seconds)


def erase(n):
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def write(sentence):
    for char in sentence:
        print(char, end='', flush=True)
        sleep(0.01)


def write_green(sentence):
    write(Fore.LIGHTGREEN_EX + sentence + Fore.RESET)


def write_cyan(sentence):
    write(Fore.CYAN + sentence + Fore.RESET)


def write_red(sentence):
    write(Fore.RED + sentence + Fore.RESET)


def empty():
    clear()
    sleep(0.5)
    list_tasks.clear()
    check_list()
    choice_option()


def add_task():
    clear()
    sleep(0.5)
    task_name = input(Fore.CYAN + "Enter the name of the task : " + Fore.RESET)
    list_tasks.append(task_name)
    clear()
    sleep(0.5)
    check_list()
    choice_option()


def remove_task():
    clear()
    sleep(0.5)
    clear()
    check_list()
    sleep(0.5)
    while True:
        try:
            index_task = int(input(Fore.CYAN + "\n\nNumber of the task you want to remove: " + Fore.RESET))
            if 1 <= index_task <= len(list_tasks):
                break
            else:
                write_red("\nChoose an existing task!")
                sleep(2)
                erase(4)
        except ValueError:
            write_red("\nPlease enter a valid digit!")
            sleep(2)
            erase(4)
    clear()
    sleep(0.5)
    list_tasks.pop(index_task - 1)
    clear()
    sleep(0.5)
    check_list()
    choice_option()


def edit_task():
    clear()
    sleep(0.5)
    clear()
    check_list()
    sleep(0.5)
    try:
        index_task = int(input(Fore.CYAN + "\n\nNumber of the task do you want to edit : " + Fore.RESET))
    except ValueError:
        write_red("\nPlease enter a digit !")
        sleep(2)
        erase(4)
        edit_task()
    if 1 <= index_task <= len(list_tasks):
        pass
    else:
        write_red("\nChoose an existing task !")
        sleep(2)
        erase(4)
        edit_task()
    clear()
    sleep(0.5)
    list_tasks[index_task - 1] = input(Fore.CYAN + "Enter the new name of the task : " + Fore.RESET)
    clear()
    sleep(0.5)
    check_list()
    choice_option()


def help():
    clear()
    sleep(0.5)
    write_green("Here are all the available options : ")
    sleep(2)
    print("")
    write_green("\n0 = HELP\n1 = ADD TASK\n2 = REMOVE TASK\n3 = EDIT TASK\n4 = EMPTY LIST\n5 = EXIT PROGRAM")
    sleep(6)
    clear()
    check_list()
    choice_option()


def exit_program():
    clear()
    sleep(0.1)
    sys.exit()


# THE USER CHOOSE AN OPTION

def choice_option():
    while True:
        try:
            choice = int(input(Fore.CYAN + "\n\nChoose an option (0 for help) : " + Fore.RESET))
        except ValueError:
            write_red("\nPlease enter a valid digit !")
            sleep(2)
            erase(4)
            continue
        if choice in options:
            if choice == options[0]:
                help()
            elif choice == options[1]:
                add_task()
            elif choice == options[2]:
                if len(list_tasks) == 0:
                    write_green("\nThe list is empty.")
                    sleep(2)
                    clear()
                    check_list()
                    choice_option()
                else:
                    remove_task()
            elif choice == options[3]:
                if len(list_tasks) == 0:
                    write_green("\nThe list is empty.")
                    sleep(2)
                    clear()
                    check_list()
                    choice_option()
                else:
                    edit_task()
            elif choice == options[4]:
                empty()
            elif choice == options[5]:
                exit_program()
        else:
            write_red("\nChoose a valid digit !")
            sleep(2)
            erase(4)


# CHECK LIST

def check_list():
    sleep(0.01)
    save_tasks()
    if not list_tasks:
        write_green("Your TO-DO List is empty.")
    else:
        write_green("You have " + Fore.LIGHTWHITE_EX + str(len(list_tasks)) + Fore.GREEN + " tasks to do:" + Fore.RESET)
        for i, task in enumerate(list_tasks, 1):
            write_green("\n\n{}. {}".format(i, task))


# START

clear()
check_list()
choice_option()
