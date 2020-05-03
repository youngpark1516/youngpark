import turtle
import time
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(0)

#functions
def star(x=15):
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(x)
    turtle.left(144)
    turtle.forward(x)
    turtle.left(144)
    turtle.forward(x)
    turtle.left(144)
    turtle.forward(x)
    turtle.left(144)
    turtle.forward(x)
    turtle.left(144)
    turtle.end_fill()

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def square(x, y):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)

def home():
    turtle.penup()
    turtle.home()
    turtle.pendown()

def dist(x, y):
    return turtle.distance(x, y)

#틀
move(-300, -200)
square(600,400)
# move(-300, 200)
# turtle.goto(300,-200)
# move(-300,-200)
# turtle.goto(300,200)

#문양 layer 1
move(0, -100)
turtle.color("blue")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#문양 layer 2
move(0,0)
turtle.color("red")
turtle.begin_fill()
turtle.left(56.31)
turtle.circle(50)
turtle.end_fill()

#문양 layer 3
move(83.21, -55.46)
turtle.begin_fill()
turtle.circle(100,180)
move(83.21, -55.46)
turtle.goto(-83.21, 55.46)
turtle.end_fill()

#문양 layer 4
move(83.21, -55.46)
turtle.color("blue")
turtle.left(123.69)
turtle.left(56.31)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#리셋
turtle.color("black")
home()

#건괘 layer 1
move(-155.47, 41.61)
turtle.left(56.31)
turtle.begin_fill()
square(100,66.66)
turtle.end_fill()

#건괘 layer 2
move(-169.33, 50.85)
turtle.color("white")
turtle.begin_fill()
square(101, 8.33)
turtle.end_fill()

#건괘 layer 3
move(-190.12, 64.71)
turtle.begin_fill()
square(101, 8.33)
turtle.end_fill()

home()

#곤괘 layer 1
turtle.color("black")
move(155.47, -161.79)
turtle.left(56.31)
turtle.begin_fill()
square(100, 66.66)
turtle.end_fill()

#곤괘 layer 2
turtle.color("white")
move(141.61, -152.55)
turtle.begin_fill()
square(101, 8.33)
turtle.end_fill()

#곤괘 layer 3
move(120.82, -138.64)
turtle.begin_fill()
square(101, 8.33)
turtle.end_fill()

#곤괘 layer 4
turtle.pensize(8.33)
move(225, -150)
turtle.goto(100, -66.66)

home()

#이괘 layer 1
turtle.pensize(1)
turtle.color("black")
move(-155.47 , -161.79)
turtle.left(33.69)
turtle.begin_fill()
square(66.66, 100)
turtle.end_fill()

#이괘 layer 2
move(-141.61, -152.55)
turtle.color("white")
turtle.begin_fill()
square(8.33, 101)
turtle.end_fill()

#이괘 layer 3
move(-120.82, -138.69)
turtle.begin_fill()
square(8.33, 101)
turtle.end_fill()

#이괘 layer 4
turtle.pensize(8.3)
move(-225, -150)
turtle.goto(-100, -66.66)

#이괘 layer 5
turtle.pensize(1)
turtle.color("black")
move(-155.47 , -161.79)
turtle.begin_fill()
square(15, 100)
turtle.end_fill()

#이괘 layer 6
move(-113 , -134)
turtle.begin_fill()
square(16, 100)
turtle.end_fill()

home()

#감괘 layer 1
move(155.47, 41.61)
turtle.left(33.69)
turtle.begin_fill()
square(66.66, 100)
turtle.end_fill()

#감괘 layer 2
move(169.33, 50.85)
turtle.color("white")
turtle.begin_fill()
square(8.33, 101)
turtle.end_fill()

#감괘 layer 3
move(190.12, 64.71)
turtle.begin_fill()
square(8.33, 101)
turtle.end_fill()

#감괘 layer 4
turtle.pensize(8.3)
move(225, 150)
turtle.goto(100, 66.66)

#감괘 layer 5
turtle.pensize(1)
turtle.color("black")
move(176.26, 55.47)
turtle.begin_fill()
square(16, 100)
turtle.end_fill()



time.sleep(15)