from turtle import Turtle, Screen
import random


def step(ttl):
    ttl.forward(random.randint(0, 10))


scn = Screen()
scn.setup(width=500, height=400)

colours = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']
start = -75
turtles = []
race_is_on = False

for colour in colours:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(-250, start)
    start += 30
    turtles.append(new_turtle)

bet = scn.textinput(title='Make your bet',
                    prompt='Which turtle will win the race?')

if bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner_colour = turtle.pencolor()
            race_is_on = False
            if winner_colour == bet:
                print(f"You win! The {winner_colour} turtle came first!")
            else:
                print(f"You lost! The {winner_colour} turtle came first!")
            break
        step(turtle)

scn.exitonclick()
