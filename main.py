import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor('blue')
t.pensize(2)
t.circle(35)
t.penup()

t.goto(0,15)
t.pendown()
t.pencolor('black')
t.circle(35)
t.penup()

t.goto(80,15)
t.pendown()
t.pencolor('red')
t.circle(35)
t.penup()

t.goto(-40,-15)
t.pendown()
t.pencolor('yellow')
t.circle(35)

t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor('green')
t.circle(35)

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('purple')
t.write("Winter Olympics",font=("bold", 30, "bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('purple')
t.write("2026",font=("bold", 30, "bold italic"),align="center")


turtle.done()