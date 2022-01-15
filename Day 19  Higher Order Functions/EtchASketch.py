from turtle import Turtle, Screen, backward, right

ttl = Turtle()
scn = Screen()


def turn_right():
    ttl.right(5)


def turn_left():
    ttl.left(5)


def forwards():
    ttl.forward(10)


def backwards():
    ttl.backward(10)


scn.listen()
scn.onkey(key='w', fun=forwards)
scn.onkey(key='a', fun=turn_left)
scn.onkey(key='s', fun=backwards)
scn.onkey(key='d', fun=turn_right)

scn.exitonclick()
