import turtle
pen = turtle.Turtle()
# print(pen.xcor())
# print(pen.ycor())
def move():
    pen.forward(10)
    if pen.xcor()<200:
        turtle.ontimer(move,1000)
move()
turtle.done()