import turtle
x=50
i=0
m=0
n=0
turtle.goto(m,n)
for i in range(10):
    i=i+1
    x=x+40
    turtle.shape('turtle')
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    m=m-20
    n=n-20
    turtle.penup()
    turtle.goto(m,n)
    turtle.pendown()





