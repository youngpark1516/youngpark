#1. 지붕이 이쓸것
#2. 서로다른 모양의 차무니 두개이상 이쓸것
#3. 추립무니 이쓸것 (손자비 포함)
#4. 바마늘엔 보름달하나와 별드리 바바박
#5. 알록달록

import turtle
import random
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

def secggal():
    color = ["red","blue","orange","yellow","green","navy","purple"]
    turtle.color(random.choice(color))


def square(x, y):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
#별
for i in range(30):
    move(random.randint(-200, 350),random.randint(100, 400))
    star()

#틀
move(-100,-100)
turtle.color("brown")
turtle.begin_fill()
square(300,150)
turtle.end_fill()

#창문 1
move(-25,-25)
for i in range(4):
    secggal()
    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
#창문 2
move(125,-45)
secggal()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.color("black")
turtle.circle(25)
move(100, -20)
turtle.forward(50)
move(125, -45)

turtle.left(90)
turtle.forward(50)

#문
turtle.color("black")
turtle.right(90)
move(40, -100)
secggal()
turtle.begin_fill()
square(35,75)
turtle.end_fill()

#손잡이
move(65, -65)
secggal()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
move(1000,1000)

#지붕
move(200, 50)
secggal()
turtle.begin_fill()
turtle.left(120)
turtle.forward(40)
turtle.left(60)
turtle.forward(260)
turtle.left(60)
turtle.forward(40)
turtle.left(120)
turtle.forward(300)
turtle.end_fill()

time.sleep(3)