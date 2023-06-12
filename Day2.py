# Primitive data types

# Strings --> string of characters; require double quotes

# print("Hello"[0])
# prints out the character located at that index

# string concatenation --> print("123" + "345")

# Integer --> whole numbers, no decimal places

# print(123 + 345) # 123456789 == 123_456_789

# Float --> 3.14159

# Boolean --> True or False

# type() --> returns the data type of the variable; type checking

####### type casting --> converts one data type into another

# converting data type

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")
# other type cast functions --> float, str, int

# Challenge 2.1

# num = input("Please enter a number: ")

# num1 = int(num[0])
# num2 = int(num[1])

# sum = num1 + num2

# print(sum)

# Math operators --> +, -, *, /

# whenever we perform division, a float is returned

# ** is the exponent operator

# PEDMAS

# Challenge 2.2

# weight = input("Please enter your weight in kg: ")
# height = input("Please enter your height in m: ")

# new_weight = float(weight)
# new_height = float(height)

# bmi = int(new_weight / new_height ** 2)

# print("Your BMI is: " + str(bmi))


##### Modifying numbers

# rounding --> round(8 / 3, 2) --> round number to two decimal places

# can also use floor --> 8 // 3

# += --> incrementing; equivalent to score = score + 1

# f-strings --> go in front of string; allow us to make converting values into strings easier

# example --> print(f "your score is {score} "


# Challenge 2.3

# How many days, weeks, and months do we have left until we're 90?

# 1 year = 365 days, 52 weeks, 12 months

#age = input("What is your current age? ")

#years_until_90 = int(90 - int(age))

# days_until_90 = int(years_until_90 * 365)
# weeks_until_90 = int(years_until_90 * 52)
# months_until_90 = int(years_until_90 * 12)

# print(f"You have {days_until_90} days, {weeks_until_90} weeks, and {months_until_90} months left.")

# Day 2 Project --> Tip Calculator

print("Welcome to the tip calculator.\n")
total_bill = input("What was your total bill? $")
tip_percent = input("What percentage tip would you like to give? 10%, 12%, or 15%? ")
amount_people = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
tip_percent_float = float(tip_percent)
amount_people_int = int(amount_people)

new_tip_per = tip_percent_float / 100
new_bill = total_bill_float * new_tip_per
total_sum = total_bill_float + new_bill
final_tip = total_sum / amount_people_int

print(f"Each person should pay ${round(final_tip,2)}")







