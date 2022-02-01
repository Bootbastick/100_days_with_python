import random
from time import sleep
import turtle
t = turtle.Turtle()
color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray1", "white"]
directions = [0, 90, 180, 270]
t.pensize(15)
t.speed("fastest")


for i in range(random.randint(200, 10000)):
    t.color(random.choice(color_list))
    t.forward(30)
    t.setheading(random.choice(directions))


turtle.exitonclick()