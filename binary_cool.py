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
    os.system("clear")

clear()

# The calabration is used to see how many ones and zeros to put on the screen
calabration = len(input(f"{colors.OKCYAN}Put as many 0 as it needs to make a line across your screen\n"))

# Sometimes the lines go by too fast, so we ask the user for the delay
delay = float(input("Delay: "))

# This is sets the chance of getting a space instead of a one and zero
space_number = int(input("Chance of space: "))

# Makes it stop showing the color cyan for text
print(colors.ENDC)

# Make a list of the numbers to get lines to work currectly
number_list = []

# Make the screen clear at the end of the script
atexit.register(clear)

clear()

# Set up an infinite loop
while True:
    # A loop based on the calabration to make the line
    for i in range(calabration):
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