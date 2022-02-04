import turtle
tim = turtle

t = turtle.Turtle()


def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_anti_clockwise():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def turn_clockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear_drawing():
    turtle.resetscreen()

def diagonaly_left():
    t.left(1)
    t.forward(1)


tim.listen()
# if tim.onkeypress(key="w") and tim.onkeypress(key="a"):
#     t.circle(extent=1)
tim.onkeypress(move_forwards, key="w")
tim.onkeypress(turn_anti_clockwise, key="a")
tim.onkeypress(move_backwards, key="s")
tim.onkeypress(turn_clockwise, key="d")
tim.onkeypress(clear_drawing, key="c")

tim.exitonclick()
