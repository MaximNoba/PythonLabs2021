import turtle
import math as np


turtle.left(90)
for i in range(100):
    for i in range(400):
        turtle.shape('turtle')
        turtle.forward(2*4*np.sin(180/800))
        turtle.right(180-180*(800-2)/800)
    for i in range(200):
        turtle.shape('turtle')
        turtle.forward(2*1*np.sin(180/400))
        turtle.right(180-180*(400-2)/400)
