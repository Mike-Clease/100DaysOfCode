from turtle import Turtle, Screen, time

# Set up screen

scn = Screen()
scn.setup(height=600, width=600)
scn.bgcolor('black')
scn.title('Snake')
scn.tracer(0)

start_x = [(-20, 0), (0, 0), (20, 0)]

snake = []

for pos in start_x:
    segment = Turtle(shape='square')
    segment.penup()
    segment.goto(pos)
    segment.color('white')
    snake.append(segment)

game_is_on = True

while game_is_on:
    scn.update()
    time.sleep(0.1)
    for seg in range(len(snake)-1, 0, -1):
        new_x = snake[seg-1].xcor()
        new_y = snake[seg-1].ycor()
        snake[seg].goto(new_x, new_y)
    snake[0].forward(20)


scn.exitonclick()
