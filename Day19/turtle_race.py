import random
from turtle import Turtle, Screen
import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
i = 0
all_turtles = []
red = Turtle(shape="turtle")
red.color(colors[i])
i += 1
screen = Screen()


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


red.penup()
red.goto(-230, -99)
all_turtles.append(red)


orange = Turtle(shape="turtle")
orange.color(colors[i])
i += 1
orange.penup()
orange.goto(-230, -66)
all_turtles.append(orange)


yellow = Turtle(shape="turtle")
yellow.color(colors[i])
i += 1
yellow.penup()
yellow.goto(-230, -33)
all_turtles.append(yellow)


green = Turtle(shape="turtle")
green.color(colors[i])
i += 1
green.penup()
green.goto(-230, 33)
all_turtles.append(green)


blue = Turtle(shape="turtle")
blue.color(colors[i])
i += 1
blue.penup()
blue.goto(-230, 66)
all_turtles.append(blue)


purple = Turtle(shape="turtle")
purple.color(colors[i])
i += 1
purple.penup()
purple.goto(-230, 99)
all_turtles.append(purple)
is_race_on = True


while is_race_on:
    for turtlee in all_turtles:
        if turtlee.xcor() > 230:
            print(f"Turtle of color {turtlee.pencolor()} has won the race.")
            if turtlee == user_bet:
                print("Turtle that you betted on has won the race!")
            else:
                print("Somebodies else's turtle won the race!")
            exit()
        rand_distance = random.randint(0, 10)
        turtlee.forward(rand_distance)
    
        


turtle.exitonclick()
