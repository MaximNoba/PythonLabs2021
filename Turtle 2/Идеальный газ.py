from random import randint, random
import turtle
import time
import math

number_of_turtles = 50
dt = 0.1

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.goto(-200, 200)
turtle.goto(200, 200)
turtle.goto(200, -200)
turtle.goto(-200, -200)
vx = []
vy = []
x = []
y = []
i=0
j=0
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    vx.append(200*random())
    vy.append(200*random())
    x.append(200*random())
    y.append(200*random())
    unit.speed(200)
    unit.goto(x[i], y[i])
for i,j in range(number_of_turtles - 1):
    for unit in pool:
        while True:
            y[i] += vy[j]*dt
            x[i] += vx[j]*dt
            if abs(y[i]) >= 200:
                vy[j] = -vy[j]
            if abs(x[i]) >= 200:
                vx[j] = -vx[j]    
            unit.goto(x[i], y[i])
            j += 1
            i += 1
