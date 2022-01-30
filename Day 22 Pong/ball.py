from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(45)

    def move(self):
        self.forward(10)

    def bounce(self):
        self.setheading(self.heading() * -1)

    def ricochet(self):
        if self.heading() <= 90:
            self.setheading(90 + self.heading())
        elif self.heading() <= 180:
            self.setheading(90 - (self.heading() - 90))
        elif self.heading() <= 270:
            self.setheading((270 - self.heading()) + 180)
        else:
            self.setheading(270 - (360 - self.heading()))
