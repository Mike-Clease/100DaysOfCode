from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed('fastest')

colours = ['blue', 'red', 'green', 'cyan', 'purple', 'brown',
           'orange', 'magenta', 'pink', 'purple']

screen = Screen()
screen.colormode(255)


def square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def dashes(turtle, number):
    for _ in range(number):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)


def draw_shape(turtle, sides):
    int_angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.left(int_angle)


def random_walk(turtle, total_length):
    length = 0
    while length <= total_length:
        turtle.pencolor(random_colour())
        turtle.left(random.randint(0, 360))
        len = random.randint(0, 50)
        turtle.forward(len)
        length += len


def random_colour():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return (red, green, blue)


def spirograph(turtle, size, circles):
    turtle.circle(size)
    turtle.left(360 / circles)


circles = 100
for _ in range(circles):
    timmy.pencolor(random_colour())
    spirograph(timmy, 100, circles)

# for sides in range(3, 13):
#         timmy.color(random.choice(colours))
#         draw_shape(timmy, sides)

screen.exitonclick()
