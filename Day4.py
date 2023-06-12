# Day 4 --> Randomization

# Project --> Rock Paper Scissors

import random

choice = int(input("What do you choose? 0 for rock, 1 for paper, or 2 for scissors "))

cpu_choice = random.randint(0, 2)

# Player choice is rock
if choice == 0:
    print("You chose rock.")
    if cpu_choice == 0:
        print("Computer chose rock")
        print("Draw.")
    elif cpu_choice == 1:
        print("Computer chose paper")
        print("You lose")
    else:
        print("Computer chose scissors")
        print("You win")

# Player choice is paper
elif choice == 1:
    print("You chose paper.")
    if cpu_choice == 0:
        print("Computer chose rock")
        print("You win.")
    elif cpu_choice == 1:
        print("Computer chose paper")
        print("Draw")
    else:
        print("Computer chose scissors")
        print("You lose")

# Player choice is scissors
elif choice == 2:
    print("You chose scissors.")
    if cpu_choice == 0:
        print("Computer chose rock")
        print("You lose")
    elif cpu_choice == 1:
        print("Computer chose paper")
        print("You win")
    else:
        print("Computer chose scissors")
        print("Draw")
else:
    print("Please try again.")






# AskPython --> documentation for Python

# Random module

# using random module/library

# import random

# random_integer = random.randint(1,10) # range of numbers specified
# print(random_integer)

# module --> modules are responsible for different functionalities on a project

# random_float = random.random() * 5 # random floating point number between 0.0-1.0
# print(random_float)

####### Challenge 4.1 --> Heads or Tails Program

# random_num = random.randint(0, 1)
# if random_num == 1:
#    print(f"{random_num} - Heads.")
# else:
#    print(f"{random_num} - Tails.")

# Lists --> Offset and Appending Items

# states_of_usa = ["Delaware", "Pennsylvania"]

# -1 --> last item in a list
# existing list items can be manipulated, despite already being created
# can also append new items to a list
# can use .extend method to add more items to a list as well


######## Challenge 4.2 --> Banker Roulette

# Import the random module here
# import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ") # divides string wherever a comma is present
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# num_items = len(names)

# random_name = random.randint(0, num_items-1)

# person_pay = names[random_name]

# print(person_pay + " is going to buy the meal today.")

#### Index errors and working with nested lists

# nested lists --> contain two existing lists

####### Challenge 4.3 --> Treasure Map Exercise

# 🚨 Don't change the code below 👇
# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# print(type(position))
# digits = [int(position) for position in str(position)]

# column = digits[0] - 1
# row = digits[1] - 1

# map[row][column] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

