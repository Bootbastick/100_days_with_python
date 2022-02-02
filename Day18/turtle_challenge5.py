import random
import turtle
t = turtle.Turtle()
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
turtle.colormode(255)


def draw_circle():
    t.color(random_color())
    t.circle(100)


turn = 5
range_of_turn = int(360 / turn)
for i in range(range_of_turn):
    draw_circle()
    t.left(turn)


turtle.exitonclick()