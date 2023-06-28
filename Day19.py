from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(10)

def move_right():
# tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def move_left():
# tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_backwards():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward) # parameters --> key, function
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
