# Day 3 --> Conditional Statements, Logical Operators

# Day 3 Project: Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_dir = input("First things first: Left or Right? ").lower()
if first_dir == "left":
    print("Proceed.")
    second_dir = input("Swim or wait? ").lower()
    if second_dir == "wait":
        third_dir = input("Which door? Red, blue, or yellow? ").lower()
        if third_dir == "yellow":
            print("You win!")
        elif third_dir == "red" or third_dir == "blue":
            print("Game over.")
    elif second_dir == "swim":
        print("Game over.")
elif first_dir == "right":
    print("Game over.")


# if-else operators

# depending on conditions, a or b is executed

# if (condition):
#     statement
# else:
#     statement

# indentation is important in Python, in comparison to other languages

# indentation error will show up if not indented properly

# >, <, ==, >=, <=, !=

# Challenge 3.1 --> Odd or Even Exercise

# num = int(input("Please enter a number: "))

# if num % 2 == 0:
#    print("The number is even.\n")
# else:
#    print("The number is odd.\n")

# nested if/else

# if (condition)
#   if (another condition):
#       do this
#   else:
#       do this

# else (condition):
#       do this

# can also use elif statements

# if condition1:
#    statement
# elif condition2:
#    statement
# else:

# Day 3.2 --> BMI Calculator 2.0

# height = float(input("Please enter your height in m: "))
# weight = float(input("Please enter your weight in kg: "))

# bmi = weight / (height * height)
# print(f"Your bmi is: {round(bmi,-1)}")

# if bmi < 18.5:
#  print("Underweight\n")
# elif bmi == 18.5 or bmi < 24.9:
#   print("Normal weight\n")
# elif bmi == 25 or bmi < 29.9:
#    print("Overweight.\n")
# elif bmi >= 30:
#   print("Obesity.\n")
# else:
#    print("Please try again.\n")

# Exercise: Determining a leap year
# Def of leap year --> On every year that is divisible by 4, except every year divisible by 100
#                unless the year is also evenly divisible by 400

# year = int(input("Please enter a year: "))

#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print(f"{year} is a leap year")
#        else:
#            print(f"{year} is not a leap year")
#    else:
#        print(f"{year} is a leap year")
#else:
#    print(f"{year} is not a leap year")

# Multiple if-statements

# Day 3.4 --> Pizza Order Program

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza would you like? S, M, L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# price = 0

# if size == "S":
#    price += 15
#    if add_pepperoni == "Y":
#        price += 2
# if size == "M":
#    price += 20
#    if add_pepperoni == "Y":
#        price += 3
# if size == "L":
#    price += 25
#    if add_pepperoni == "Y":
#        price += 3
# if extra_cheese == "Y":
#    price += 1
# print(f"Total price: ${price}")

# Logical operators

# and, or, not

# Challenge 3.5 --> Love Calculator
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# new_name1 = name1.lower()
# new_name2 = name2.lower()

# name_string = new_name1 + new_name2

# t = name_string.count('t')
# r = name_string.count('r')
# u = name_string.count('u')
# e = name_string.count('e')

# true_score = t + r + u + e

# l = name_string.count('l')
# o = name_string.count('o')
# v = name_string.count('v')
# e = name_string.count('e')

# love_score = l + o + v + e

# final_score = int(str(true_score) + str(love_score))

# if final_score < 10 or final_score > 90:
#    print(f"Your score is {final_score}, you go together like Coke and Mentos.")
# elif final_score > 40 and final_score < 50:
#    print(f"Your score is {final_score}, you are alright together.")
# else:
#    print(f"Your score is {final_score}.")



