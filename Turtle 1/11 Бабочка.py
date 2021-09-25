import math as np
import turtle

r=5
n=40
i=0
for i in range(10):
    for i in range(n):
        turtle.shape('turtle')
        turtle.forward(2*r*np.sin(180/n))
        turtle.left(180-180*(n-2)/n)
    for i in range(n):
        turtle.shape('turtle')
        turtle.forward(2*r*np.sin(180/n))
        turtle.right(180-180*(n-2)/n)
    r=r+1
