import turtle
import time

y = 0
x = -900
vx = 50
vy = 80
dt = 0.1
g = -9.8
k = -0.05
t = 0
turtle.shape('circle')
turtle.speed(1000)
turtle.goto(1000, 0)
turtle.goto(-1000,0)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.speed(95)
for i in range(10000000):
    x = x + vx * dt
    y = y + vy * dt + g *dt**2/2
    vy = vy + g * dt + k * vy * dt
    vx = vx + k * vx * dt
    if y <= 0:
        y = 0
        vy = -0.95*vy
        vx = 0.95*vx
    turtle.goto(x, y)
    
