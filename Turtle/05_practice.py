import turtle
pen = turtle.Turtle()
# 🧪 Practice 1

# Ek program banao jisme: Space → turtle 50 forward   b → turtle 50 backward
def move():
    pen.forward(50)
def move1():
    pen.backward(50)    
turtle.listen()
turtle.onkey(move,'space')
turtle.onkey(move1,'b')
turtle.done()