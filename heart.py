import turtle

t = turtle.Turtle()
t.speed(1)
t.pensize(5)
t.color('red', 'pink')  

t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

t.hideturtle()
turtle.done()