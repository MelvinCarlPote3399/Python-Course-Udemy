# from turtle import Turtle, Screen
# import turtle as t
import random

# turtle has dedicated documentation online

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

### Turtle Challenge 1 --> Draw a square

# def turtle_proceed():
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
#
# turtle_proceed()
# timmy_the_turtle.right(90)
# turtle_proceed()

# use an asterisk to import everything from a module; comes with disadvantages though

# we can also use aliases to refer to modules using "import turtle as ..."

# some modules aren't packaged with the standard Python; we can go online to install packages

### Turtle Challenge 2 --> Draw a dashed line

# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


### Turtle Challenge 3 --> Drawing Shapes

# colours = ["aquamarine", "chocolate4", "coral", "DarkGreen", "DarkOrchid", "DeepPink"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
# for sides in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(sides)


### Turtle Challenge 4 --> Draw a Random Walk

# colours = ["aquamarine", "chocolate4", "coral", "DarkGreen", "DarkOrchid", "DeepPink"]
#
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))

# screen = Screen()
# screen.exitonclick()

## Tuples
# values inside tuples cannot be changed or appended; immutable; complete opposite of lists (arrays)
# using list(), tuple can be converted into a list
# can use colormode() method, via the RGB codes, followed by the random.randint(0, 255)

# t.colormode(255)
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r,g,b)
#     return random_colour
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#      timmy_the_turtle.color(random_colour())
#      timmy_the_turtle.forward(30)
#      timmy_the_turtle.setheading(random.choice(directions))


### Challenge 5 --> Draw a Spirograph

# t.pensize(2)
# t.speed("fastest")
#
# for i in range(6):
#
#     # Choose your color combination
#     for color in ('red', 'magenta', 'blue',
#                   'cyan', 'green', 'white',
#                   'yellow'):
#         t.color(color)
#
#         # Draw a circle of chosen size, 100 here
#         t.circle(100)
#
#         # Move 10 pixels left to draw another circle
#         t.left(10)

## Colorgram
# colorgram.py is a useful package to extract colours from images

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()