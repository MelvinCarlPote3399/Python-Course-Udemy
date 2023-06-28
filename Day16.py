# Day 16 --> OOP (Object-Oriented Programming)

# Procedural programming was an older practice used, prior to OOP

# Object-oriented programming is like a manager in charge of a restaurant with staff doing
# other tasks

# Object-oriented programming tries to model real world objects, made up of smaller objects

# objects are made up of attributes (variables) & methods

# classes <--> objects

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("DarkSalmon")
#
# print(my_screen.canvheight) # class, followed by attribute or method
# print(timmy)
# my_screen.exitonclick() # allows program to keep on running until a click is detected

# tons of other functions/methods; refer to documentation for more methods associated with the Turtle library

# packages can be useful for projects, made by other developers

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

