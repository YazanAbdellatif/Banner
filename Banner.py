import turtle
t=turtle.Turtle()
tscreen=turtle.Screen()
t.speed(0)
t.penup()
t.goto(-300,0)
t.pendown()
t.color("cyan")
name=tscreen.textinput("enter name","what is your name")
t.write(name,font=("script",50,"bold"))
t.penup()
t.goto(150,75)
t.pendown()
t.color("red","blue")
t.begin_fill()
t.fd(50)
t.left(72)
t.fd(50)
t.right(144)
t.fd(50)
t.left(72)
t.fd(50)
t.right(144)
t.fd(50)
t.left(72)
t.fd(50)
t.right(144)
t.fd(50)
t.left(72)
t.fd(50)
t.right(144)
t.fd(50)
t.left(72)
t.fd(50)
t.right(144)
t.end_fill()
t.hideturtle()
t.penup()
turtle.done()