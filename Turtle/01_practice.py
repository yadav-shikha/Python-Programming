import turtle
pen = turtle.Turtle()
# Q1 100 pixels ki line banao.
# pen.forward(100)


# Q2 L shape banao.
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# or
# pen.forward(100)
# pen.backward(100)
# pen.left(90)
# pen.forward(100)

# Q3 100 forward jao, 100 backward aao.
# pen.forward(100)
# pen.backward(100)

# Q4 Red color ki 200 pixels ki line banao.
# pen.color('red')
# pen.forward(200)

# Q5 Pehle bina line ke 100 pixels aage jao, fir line draw karte hue 100 pixels aur aage jao.
pen.penup()
pen.forward(100)
pen.pendown()
pen.forward(100)
turtle.done()