import turtle
pen = turtle.Turtle()
# 🧪 Practice 1

# Ek program banao jisme: Space → turtle 50 forward   b → turtle 50 backward
# def move():
#     pen.forward(50)
# def move1():
#     pen.backward(50)    
# turtle.listen()
# turtle.onkey(move,'space')
# turtle.onkey(move1,'b')



# def click(x, y):
#     pen.penup()
#     pen.goto(x, y)
#     pen.dot(20, "red")
# turtle.onscreenclick(click)

# Ek program banao:

# Up press → turtle forward(10)
# Down press → turtle backward(10)
# Left press → turtle left(10)
# Right press → turtle right(10)
def forword():
    pen.forward(10)
def backward():
    pen.backward(10)
def left():
    pen.left(10)
def right():
    pen.right(10)

turtle.listen()
turtle.onkey(forword,'Up')
turtle.onkey(backward,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')

turtle.done()