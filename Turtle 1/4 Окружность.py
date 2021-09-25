import math as np
import turtle
print('Введите радиус')
r = float(input())
print('Введите число сторон вписанного правильного многоугольника, которым приближаете окружность')
n = int(input())
i=0
for i in range(n):
    turtle.shape('turtle')
    turtle.forward(2*r*np.sin(180/n))
    turtle.left(180-180*(n-2)/n)
