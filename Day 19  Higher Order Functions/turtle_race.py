from turtle import Turtle, Screen
import random


def step(ttl):
    ttl.forward(random.randint(0, 10))


scn = Screen()
scn.setup(width=500, height=400)

colour_list = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']

start_y = -75

for colour in colour_list:
    ttl = Turtle(shape='turtle')
    ttl.color(colour)
    ttl.penup()
    ttl.goto(-250, start_y)
    start_y += 30

bet = scn.textinput(title='Make your bet',
                    prompt='Which turtle will win the race?')

scn.exitonclick()
