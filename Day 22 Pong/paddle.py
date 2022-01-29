from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_square()

    def create_square(self):
        square = Turtle(shape='square')
        square.penup()
        square.color('white')
        square.goto(-350, 0)
        square.turtlesize(stretch_len=1, stretch_wid=5)
        
    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        
    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)