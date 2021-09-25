import math as np
import turtle
print('Введите число лап')
n = int(input())

for i in range(n):
  turtle.shape('turtle')
  turtle.forward(200)
  turtle.stamp()
  turtle.backward(200)
  turtle.left(360/n)

