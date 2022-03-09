from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.pencolor("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()
