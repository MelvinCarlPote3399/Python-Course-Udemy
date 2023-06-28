import turtle
from turtle import Turtle, Screen
import random
# tim = Turtle()
screen = Screen()

is_race_on = False
screen.setup(width=500, height=400) # better to use keyword arguments vs positional arguments
user_bet = screen.textinput(title="Turtle Race", prompt="Place your bet on which turtle will win: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinate = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    # random_position = random.randint(-190, 190)
    new_turtle.goto(x=-230, y=y_coordinate[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle has won!")
            else:
                print(f"You lost! The {winning_color} turtle has won!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()