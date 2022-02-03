# import colorgram
import random
import turtle
#
# num_of_colors = 34
# colors_extracted = []
#
# colors = colorgram.extract('image.jpg', num_of_colors)
# for i in range(num_of_colors):
#     rgb_tuple = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
#     colors_extracted.append(rgb_tuple)
# print(colors_extracted)
color_list = [(233, 254, 243), (252, 234, 244), (42, 2, 176), (81, 252, 177), (235, 232, 253), (224, 151, 110),
              (154, 3, 85), (5, 210, 101), (4, 138, 60), (244, 42, 125), (109, 108, 245), (251, 252, 56),
              (184, 184, 250),
              (210, 106, 6), (175, 113, 246), (35, 35, 251), (139, 1, 0), (251, 37, 35), (51, 239, 57), (222, 115, 158),
              (16, 127, 143), (86, 249, 252), (185, 43, 107), (22, 5, 103), (10, 209, 214), (97, 7, 50),
              (228, 165, 206),
              (104, 7, 4), (206, 119, 31), (10, 112, 26), (235, 166, 164), (14, 107, 110), (243, 13, 23)]
t = turtle.Turtle()
t.penup()
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turtle.colormode(255)


t.setpos((-450.00, -325.00))


for _ in range(10):
    for i in range(10):
        t.color(random_color())
        t.dot(20)
        t.forward(20 + 50 + 20)
    t.setheading(90)
    t.forward(70)
    t.left(90)
    t.forward(900)
    t.right(180)
t.hideturtle()


turtle.exitonclick()
