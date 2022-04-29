from turtle import Turtle
import random
import numpy as np

LANES = [-100, -75, -50, 50, 75, 100]
START_POS = np.arange(-380, 380, 20)


class Road:
    def __init__(self):
        self.cars = []
        self.pop_road()

    def pop_road(self):
        for lane in LANES:
            car = Car(
                position=(random.choice(START_POS), lane),
                heading=random.choice([0, 180]),
            )
            self.cars.append(car)

    def start(self):
        for car in self.cars:
            car.move()


class Car(Turtle):
    def __init__(self, position, heading):
        super().__init__()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(position)
        self.color("white")
        self.penup()
        self.shape("square")
        self.setheading(heading)

    def move(self):
        self.forward(5)

        if self.xcor() >= 400 and self.heading() == 0:
            self.goto((-400, self.ycor()))
        elif self.xcor() <= -400 and self.heading() == 180:
            self.goto((400, self.ycor()))
