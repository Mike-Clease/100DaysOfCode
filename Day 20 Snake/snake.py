from pickletools import UP_TO_NEWLINE
from turtle import Turtle

START_POS = [(-20, 0), (0, 0), (20, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            segment = Turtle(shape='square')
            segment.penup()
            segment.goto(pos)
            segment.color('white')
            self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass
