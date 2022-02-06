from turtle import Turtle

# Tried to get the bouncing based off of headings rather than coding a move
# like was done in the session, it would have been pretty codey to do
# so ended up just going with the way it's done online :-(


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(45)
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def ricochet(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
