from turtle import Turtle

from nbformat import read

ALIGNMENT = "center"
FONT = ("Arial", "24", "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("classic")
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.high_score = self.read_highscore()
        self.update()

    def read_highscore(self):
        with open("high_score.txt", "r") as f:
            score = int(f.read())
            f.close()
        return score

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score} | Higher Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update()
