from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.pencolor("white")
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=("Courier", 24, "normal"))

