from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.goto((0, -200))
        self.color("white")
        self.penup()
        self.setheading(90)

    def move(self):
        self.forward(20)
