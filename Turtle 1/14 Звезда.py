import turtle

def function(n):
    for i in range(n):
        turtle.forward(500)
        turtle.left(180 - 180/n)

turtle.left(180)
function(5)

turtle.penup()
turtle.goto(600, 0)
turtle.pendown()

function(11)
