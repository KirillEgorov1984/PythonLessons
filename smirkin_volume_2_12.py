import turtle
print(turtle.speed())
turtle.showturtle()
turtle.setup(1920, 1080)
# turtle.bgcolor('gray')
colors = ['red', 'blue', 'green']
for i in range(3):
    pensize = turtle.numinput('','')
    turtle.pencolor(colors[i])
    turtle.pensize(pensize)
    # turtle.fillcolor(colors[i])
    # turtle.begin_fill()
    turtle.circle(250)
    # turtle.end_fill()