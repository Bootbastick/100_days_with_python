from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-235, 250)
        self.write("Level: ", align="center", font=FONT)
        self.goto(-180, 250)
        self.write(self.level, align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-235, 250)
        self.write("Level: ", align="center", font=FONT)
        self.goto(-180, 250)
        self.write(self.level, align="center", font=FONT)

    def add_level(self):
        self.level += 1
