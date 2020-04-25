#1. 지붕이 이쓸것
#2. 서로다른 모양의 차무니 두개이상 이쓸것
#3. 추립무니 이쓸것 (손자비 포함)
#4. 바마늘엔 보름달하나와 별드리 바바박
#5. 알록달록

import turtle
import random
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(0)

#별
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

for i in range(15):
    turtle.penup()
    turtle.setx(random.randint(-200, 200))
    turtle.sety(random.randint(100, 200))
    turtle.pendown()
    star()

#틀
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.forward(300)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(150)
turtle.left(90)

#창문 1
turtle.penup()
turtle.goto(-25,-25)
turtle.pendown()
turtle.color("light blue")
for i in range(4):
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)

#창문 2
turtle.penup()
turtle.goto(125,-45)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.goto(100,-20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.goto(125,-45)
turtle.pendown()
turtle.left(90)
turtle.forward(50)

#문
turtle.color("black")
turtle.penup()
turtle.goto(50,-45)
turtle.pendown()
turtle.


n = 0
while(n<10000000):
    n +=1
