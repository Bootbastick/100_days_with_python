import random
from time import sleep
import turtle
t = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]
t.pensize(15)
t.speed("fastest")


for i in range(random.randint(200, 10000)):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))


turtle.exitonclick()