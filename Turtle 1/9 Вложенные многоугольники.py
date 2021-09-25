import turtle
import math as np

def c(n, x):
    for i in range(n):
        turtle.shape('turtle')
        turtle.forward(2*x*np.sin(180/n))
        turtle.left(180-180*(n-2)/n)



x=200
n=3
for i in range(10):
    turtle.right(90*(n-2)/n)
    c(n, x)
    turtle.left(90*(n-2)/n)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    n=n+1
    x=x+2
    
