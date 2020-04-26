import turtle
import time

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def home():
    turtle.penup()
    turtle.home()
    turtle.pendown()


def here():
    return turtle.position()


def dist(x, y):
    return turtle.distance(x, y)


def toward(x, y):
    return turtle.towoards(x, y)


turtle = turtle.Turtle()

turtle.shape('turtle')
turtle.speed(1)
# 태극 원
a = turtle.towards(300, -200)
turtle.right(-a)
turtle.forward(100)
# move(100,0)

turtle.pensize(3)
turtle.color('red')
turtle.begin_fill()
turtle.left(90)
turtle.circle(100, 180)
turtle.end_fill()
turtle.color('blue')
turtle.begin_fill()

turtle.circle(100, 180)
turtle.end_fill()
turtle.color('black')

home()
a = turtle.towards(-300, 200)
turtle.left(a)
turtle.forward(50)
turtle.dot(100, 'red')

home()
a = turtle.towards(300, -200)
turtle.right(-a)
turtle.forward(50)
turtle.dot(100, 'blue')

# 테두리
home()
move(-300, -200)
turtle.pensize(3)
turtle.forward(600)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(400)

time.sleep(3)