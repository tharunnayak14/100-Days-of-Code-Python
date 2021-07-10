from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level {self.user_level}", align="center", font=FONT)

    def increase_level(self):
        self.user_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", True, align="center", font=FONT)
