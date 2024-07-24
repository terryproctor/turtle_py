import random
from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.width(8)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def random_walk(turtle_object, steps):
    for _ in range(steps):
        turtle_object.color(random_color())
        turtle_object.forward(20)
        turtle_object.setheading(random.choice([0, 90, 180, 270]))

random_walk(timmy, 500)

screen.exitonclick()