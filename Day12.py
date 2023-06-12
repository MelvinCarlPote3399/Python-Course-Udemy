# Day 12 --> Scope & Number Guessing Game

# Local scope --> variables are only accessible within the function
# Global scope --> variables are accessible anywhere within the program

# No block scope in Python
# Variables declared in a loop or if-statement have global scope,
# unless loop is inside a function

# use 'global' keyword to modify a global variable inside a function

### Constants and Global Scope

# Constants hold a value, with no intention of changing it
from random import randint

logo = """
#     #                                        #####                                                  #####                       
##    # #    # #    # #####  ###### #####     #     # #    # ######  ####   ####  # #    #  ####     #     #   ##   #    # ###### 
# #   # #    # ##  ## #    # #      #    #    #       #    # #      #      #      # ##   # #    #    #        #  #  ##  ## #      
#  #  # #    # # ## # #####  #####  #    #    #  #### #    # #####   ####   ####  # # #  # #         #  #### #    # # ## # #####  
#   # # #    # #    # #    # #      #####     #     # #    # #           #      # # #  # # #  ###    #     # ###### #    # #      
#    ## #    # #    # #    # #      #   #     #     # #    # #      #    # #    # # #   ## #    #    #     # #    # #    # #      
#     #  ####  #    # #####  ###### #    #     #####   ####  ######  ####   ####  # #    #  ####      #####  #    # #    # ###### 
"""
# actual_number = random.randint(1, 100)
# number_of_guesses = None
# continue_program = True
# print(f"Hello. Welcome to: \n {logo}")
#
# difficulty_level = input("Choose your difficulty: Easy or hard? ")
#
# if difficulty_level == "easy":
#     number_of_guesses = 10
# elif difficulty_level == "hard":
#     number_of_guesses = 5
#
# print(f"You have {number_of_guesses} guesses remaining.")
# user_number = int(input("Please enter a number between 1 - 100: "))
#
# for i in range(number_of_guesses-1):
#     if user_number < actual_number:
#         number_of_guesses -= 1
#         print(f"Too low!\nYou have {number_of_guesses} guesses remaining.\nPlease try again.")
#         user_number = int(input("Please enter a number between 1 - 100: "))
#     elif user_number > actual_number:
#         number_of_guesses -= 1
#         print(f"Too high!\nYou have {number_of_guesses} guesses remaining.\nPlease try again.")
#         user_number = int(input("Please enter a number between 1 - 100: "))
#     elif user_number == actual_number:
#         print(f"You guessed correctly!\nGuesses remaining: {number_of_guesses}")
#         continue_program = False
#
#     if number_of_guesses == 0:
#         print("Out of guesses.\nPlease try again!")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
#  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()