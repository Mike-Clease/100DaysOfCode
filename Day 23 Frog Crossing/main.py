from turtle import Screen, time, Turtle
from cv2 import COLOR_BGRA2RGB

from numpy import arange
import random

from player import Player
from car import Road
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Arial", "24", "normal")

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
road = Road()
board = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)

    road.start()

    # Handle Collisions
    for car in road.cars:
        dist = abs(player.distance(car))
        if dist <= 5:
            game_on = False
            board.game_over()

screen.exitonclick()
