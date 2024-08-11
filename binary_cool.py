#!/bin/python3

# Cool imports
import os
import random
import time
import atexit

# Cool Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Make the class have easy access
colors = bcolors()

# Make something to clear the console
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Setting up a character list
character_list = ["~", "`", "1", "!", "2", "@", "3", "#", "4", "$", "5", "%", "6", "^", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "{", "]", "}", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", ":", "'", '"', "\\", "|", "z", "x", "c", "v", "b", "n", "m", ",", "<", ".", ">", "/", "?"]

def true_false():
    tfl = [True, False]
    return random.choice(tfl)

def random_character(random_case:bool=False):
    character = random.choice(character_list)
    if random_case == True:
        rand_case = true_false()
        if rand_case == True:
            character = character.upper()
        if rand_case == False:
            character = character.lower()
    return character

# Clears the console screen
clear()

# The calabration is used to see how many ones and zeros to put on the screen
calabration = len(input(f"{colors.OKCYAN}Put as many 0 as it needs to make a line across your screen\n"))

# Make loop to make it easy to not have to restart the script on a fail
while True:
    # The try is used if the user forgets what a number is
    try:
        # Fix color problems
        print(colors.OKCYAN)
        # Sometimes the lines go by too fast, so we ask the user for the delay
        print("Please set a delay for the loop, I recommend either 0.01 or 0.001")

        # Get the user input then change it into a decimal able to be used in the script
        delay = float(input("Delay: "))
        
        # Then end the loop to not be stuck retyping variables
        break
    except Exception:
        # Tell the user that they messed up
        print(f"{colors.FAIL}It needs to be a number{colors.ENDC}")

# Make loop to make it easy to not have to restart the script on a fail
while True:
    # The try is used if the user forgets what a number is
    try:
        # Fix color problems
        print(colors.OKCYAN)
        # This is sets the chance of getting a space instead of a one and zero
        print("Choose a number higher than 1 to get spaces or choose 1 to get no spaces.\nI recommend setting this to 5.")

        # Get the user input then change it into a number then add 1 so the script does not completly break
        space_number = int(input("Chance of space: ")) +1
        
        # Then end the loop to not be stuck retyping variables
        break

    except Exception:
        # Tell the user that they messed up again
        print(f"{colors.FAIL}It needs to be a number{colors.ENDC}")

# Fix color problems
print(colors.OKCYAN)

# This is sets the random character flag
print("Do you want to use random characters?")

# Get the user input on using random characters
random_character_choice = input("Characters (y/N): ")

# Get options setting correctly
if random_character_choice.lower() == "y":
    random_character_choice = True

    # This is sets the random character casing flag
    print("Do you want to use random casing?")

    random_case = input("Random Casing (Y/n): ")
    if random_case.lower() == "y" or random_case.replace(" ", ""):
        random_case = True
    else:
        random_case = False
else:
    random_character_choice = False

# Make sure that the user does not make the script die so if the number is 0 or less than 0 set it to 1
if space_number <= 0:
    # The reason the number 1 was used because it will do a number between 0 - 1
    space_number = 1

# Makes it stop showing the color cyan for text
print(colors.ENDC)

# Make a list of the numbers to get lines to work currectly
number_list = []

# Make the screen clear at the end of the script
atexit.register(clear)

# Clear the console, man I write to many comments so most of my vs code is now green lol
clear()

# Set up an infinite loop
while True:
    # A loop based on the calabration to make the line
    for i in range(calabration):
        # Setting up either random character or number
        if random_character_choice == True:
            # The randomizer for the script
            rand_stuff = random.randint(0, space_number)

            # Checks if the number is greater than zero and if it is replace it with a space
            if rand_stuff >= 2:
                rand_stuff = " "
            else:
                rand_stuff = random_character(random_case)

        else:
            # The randomizer for the script
            rand_stuff = random.randint(0, space_number)

            # Checks if the number is greater than zero and if it is replace it with a space
            if rand_stuff >= 2:
                rand_stuff = " "
        
        # Add that number or space to the list
        number_list.append(str(rand_stuff))

    # After the numbers and spaces are added combine them together into a string
    number_line = ''.join(number_list)

    # Then print it out into green text
    print(f"{colors.OKGREEN}{number_line}{colors.ENDC}")

    # Last reset the list
    number_list = []

    # Then run a delay to have a bit of time between each line
    time.sleep(delay)

"""
This was not made by Chat GPT, I just put too many comments in scripts
But hey at least it's understandable to people
"""
