import turtle
import random
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(5)

# turtle.color("blue")
# turtle.pensize(4)
# turtle.circle(50)
# turtle.penup()
# turtle.sety(-50)
# turtle.setx(50)
# turtle.pendown()
# turtle.color("yellow")
# turtle.circle(50)
# turtle.penup()
# turtle.sety(0)
# turtle.setx(100)
# turtle.pendown()
# turtle.color("black")
# turtle.circle(50)
# turtle.penup()
# turtle.sety(-50)
# turtle.setx(150)
# turtle.pendown()
# turtle.color("green")
# turtle.circle(50)
# turtle.penup()
# turtle.sety(0)
# turtle.setx(200)
# turtle.pendown()
# turtle.color("red")
# turtle.circle(50)
def star(x=25):
    turtle.color("red")
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
def secggal():
    color = ["red","blue","orange","yellow","green","navy","purple"]
    turtle.color(random.choice(color))

for i in range(10):
    star(random.randint(50,100))

    turtle.penup()
    turtle.setx(random.randint(-100,100))
    turtle.sety(random.randint(-100,100))
    turtle.pendown()
    secggal()


n = 0
while(n<10000000):
    n +=1
