import turtle
import random
t = turtle.Turtle()
color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
corner = 3


def draw_a_corner_shape_8_times(corner, color_list):
    for _ in range(8):
        color = random.choice(color_list)
        t.color(color)
        for i in range(corner):
            t.right(360 / corner)
            t.forward(100)
        corner += 1
draw_a_corner_shape_8_times(corner, color_list)


turtle.exitonclick()