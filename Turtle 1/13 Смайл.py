import turtle
import math as np

def hc(x):
    for i in range(100):
         turtle.shape('turtle')
         turtle.forward(2*x*np.sin(1.8))
         turtle.left(180-180*0.98)

turtle.fillcolor('yellow')
turtle.begin_fill()
hc(5)
turtle.end_fill()

turtle.penup()
turtle.goto(-60, 200)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
hc(0.5)
turtle.end_fill()

turtle.penup()
turtle.goto(60, 200)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
hc(0.5)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 210)
turtle.pendown()
turtle.pensize(10)
turtle.right(100)
turtle.forward(80)
turtle.left(100)
turtle.forward(30)

turtle.penup()
turtle.goto(-80,150)
turtle.pendown()
turtle.right(90)
turtle.pencolor('red')
for i in range(50):
    turtle.shape('turtle')
    turtle.forward(5*np.sin(1.8))
    turtle.left(180-180*0.98)
