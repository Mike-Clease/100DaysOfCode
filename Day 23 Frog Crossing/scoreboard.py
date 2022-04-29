from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", "24", "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.shape("classic")
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
