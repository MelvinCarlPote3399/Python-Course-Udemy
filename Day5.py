# Day 5 --> Beginner - Python Loops

# Final project --> password generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

finalPassword = []
i = 0

for i in range(nr_letters):
    randomCharacters = random.choice(letters)
    finalPassword.append(randomCharacters)
for i in range(nr_symbols):
    randomNumber = random.choice(numbers)
    finalPassword.append(randomNumber)
for i in range(nr_symbols):
    randomSymbols = random.choice(symbols)
    finalPassword.append(randomSymbols)
random.shuffle(finalPassword)
print("Your password will be: " + "".join(finalPassword))




##### For loop with Python loops

# For Loop --> for item in list_of_items --> do something to each item

#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
#    print(fruit)

### Challenge 5.1 --> Average Height

# student_heights = input("Input a list of student heights: ").split()
# for n in range(0,len(student_heights)):
#    student_heights[n] = int(student_heights[n])
# print(student_heights)

# average_height = 0
# for i in range(0, len(student_heights)):
#    average_height += int(student_heights[i])
# final_average = average_height / len(student_heights)
# print(f"Average height of student is {final_average}")

### Challenge 5.2 --> High Score

# student_scores = input("Input a list of numbers: ").split()
# for n in range(0, len(student_scores)):
#    student_scores[n] = int(student_scores[n])
# print(student_scores)
# student_scores.sort()
# print(f"The largest number in the list is: {student_scores[-1]}")

### for loops and range function

# range is useful for when one does not want to work with lists
# also useful for when wanting to generate a range of numbers to loop through
# syntax --> (start, stop, step)

### Day 5.3 --> Adding Even Numbers

# sum = 0
# for i in range(0,101,2):
#    print(i)
#    sum += i
# print(f"The sum of all the even numbers from 1 to 100 is {sum}")

### Day 5.4 --> Fizz Buzz Exercise

#for i in range(1,101):
#    if i % 3 == 0 and i % 5 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(i)
