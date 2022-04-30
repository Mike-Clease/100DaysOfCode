from turtle import Turtle, Screen, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up screen

scn = Screen()
scn.setup(height=600, width=600)
scn.bgcolor("black")
scn.title("Snake")
scn.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

scn.listen()
scn.onkey(snake.up, "Up")
scn.onkey(snake.down, "Down")
scn.onkey(snake.left, "Left")
scn.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    scn.update()
    time.sleep(0.1)
    snake.move()

    # Detect eating food
    if snake.head.distance(food) < 15:
        food.refresh()
        board.increase_score()
        snake.grow()

    x_out = snake.head.xcor() > 300 or snake.head.xcor() < -300

    y_out = snake.head.ycor() > 300 or snake.head.ycor() < -300

    if x_out or y_out:
        board.reset()
        snake.reset()

    # Detect tail collision
    # if snake.head.position() game over
    for segment in snake.segments[1:]:
        dist = abs(snake.head.distance(segment))
        if dist < 10:
            board.reset()
            snake.reset()

scn.exitonclick()
