from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
