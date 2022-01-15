from turtle import Turtle, Screen, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Set up screen

scn = Screen()
scn.setup(height=600, width=600)
scn.bgcolor('black')
scn.title('Snake')
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

    # Detech wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        board.game_over()

scn.exitonclick()
