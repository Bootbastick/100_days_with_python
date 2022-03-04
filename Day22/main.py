import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
RIGHT_PADDLE_POS = (350, 0)
STRETCH_LEN = 5
LENGTH_OF_PADDLE = 5
WIDTH_OF_PADDLE = 20
POSITION_OF_RIGHT_PADDLE = (350, 0)
screen = Screen()
segments = []
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.tracer()
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # Detect collision with the walls.
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # Detect collision with the r_paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.x_move += 5
        ball.y_move += 5
    # Detect collision with the l_paddle.
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.x_move += 5
        ball.y_move += 5
    # Detect a R paddle miss.
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        ball.bounce_x()
    # Detect a L paddle miss.
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        ball.bounce_x()

screen.exitonclick()
