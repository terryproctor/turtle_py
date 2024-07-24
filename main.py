from turtle import Turtle
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def draw_shape(turtle_object, sides):
    turtle_object.color(random_color())

    for j in range(sides):
        angle = 360 / sides
        turtle_object.forward(2)
        turtle_object.right(angle)

for s in range(2, 240):
    draw_shape(timmy, s)