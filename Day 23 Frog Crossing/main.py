from turtle import Screen, time

from player import Player


screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player((0, -200))

screen.listen()
screen.onkey(player.move, "w")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
