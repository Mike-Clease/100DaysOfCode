from turtle import Turtle, Screen
import random


def step(ttl):
    ttl.forward(random.randint(0, 10))
    
    
# class racer(Turtle):
    
#     def __init__(self, x_pos, y_pos, name, colour):
#         self.position = self.goto(x_pos, y_pos)
#         self.name = name
#         self.colour = colour
#         self.shape = self.shape('Turtle')

scn = Screen()
scn.setup(width=500, height=400)

red = Turtle(shape='turtle')
green = Turtle(shape='turtle')
blue = Turtle(shape='turtle')
purple = Turtle(shape='turtle')
yellow = Turtle(shape='turtle')
orange = Turtle(shape='turtle')

red.penup()
green.penup()
blue.penup()
purple.penup()
yellow.penup()
orange.penup()

red.goto(-220, 15)
green.goto(-220, 45)
blue.goto(-220, 75)
purple.goto(-220, -15)
yellow.goto(-220, -45)
orange.goto(-220, -75)



bet = scn.textinput(title='Make your bet', prompt='Which turtle will win the race?')

scn.exitonclick()
