from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()
        else:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()
        else:
            pass

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.goto(position)
        segment.color("white")
        self.segments.append(segment)

    def grow(self):
        # add new segment to the snake
        last_seg = self.segments[-1].position()
        self.add_segment(last_seg)
