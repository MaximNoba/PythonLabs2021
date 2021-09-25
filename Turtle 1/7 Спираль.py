import math as np
import turtle

def grad(x):
     grad = ( np.sin(x) + x*np.cos(x)) / ( np.cos(x) - x*np.sin(x) ) 
     return(grad)
    
print('Введите шаг спирали на радиан изменения угла')
k = float(input())
print('Введите натуральное n для определения шага поворота угла, шаг=180 градусов/n')
n = int(input())
A=0

for i in range(100000):
    turtle.shape('turtle')
    A = A + 180/n
    turtle.left( 180*abs(abs(np.atan(grad(A+180/n))) - abs(np.atan(grad(A)))) / np.pi )
    turtle.goto(k*A*np.cos(A),k*A*np.sin(A))
    
