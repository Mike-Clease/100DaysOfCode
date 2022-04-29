from turtle import Screen, time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # right paddle collision

    if ball.xcor() >= 370 and ball.distance(right_paddle) <= 50:
        ball.ricochet()

    # left paddle collision

    if ball.xcor() <= -370 and ball.distance(left_paddle) <= 50:
        ball.ricochet()

    if ball.xcor() < -400:
        scoreboard.increase_score("Player 2")
        ball.reset()

    if ball.xcor() > 400:
        scoreboard.increase_score("Player 1")
        ball.reset()

screen.exitonclick()
