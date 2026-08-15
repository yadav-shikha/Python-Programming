import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
# Q1 Black background par white square banao.
screen.bgcolor('black')
pen.pencolor('white')
pen.width(3)
pen.speed(3)
# for i in range(4):
#     pen.forward(100)
#     pen.right(90)

# Q2 Yellow fill wala circle banao.
# pen.fillcolor('yellow')
# pen.begin_fill()
# pen.circle(100)
# pen.end_fill()

# Q3 5 alag colors ki lines banao.
colors = ['red','blue','orange','pink','green']
# import random
# for i in range(5):
#     pen.pencolor(random.choice(colors))
#     pen.forward(100)
#     pen.penup()
#     pen.forward(100)
#     pen.pendown()


# for color in colors:
#     pen.pencolor(color)
#     pen.forward(100)
#     pen.penup()
#     pen.goto(0, pen.ycor()-30)
#     pen.pendown()

# Q4 Turtle ki shape "triangle" kar do.
# pen.shape('triangle')

# Q5 Drawing ke baad turtle ko hide kar d
pen.hideturtle()


# Ek Indian Flag banane ki koshish karo:

# Orange stripe
# White stripe
# Green stripe
# Beech me blue circle (Ashoka Chakra ka simple version)
pen.penup()
pen.goto(-150,100)
pen.pendown()
pen.fillcolor('orange')
pen.begin_fill()
for i in range(2):
    pen.forward(300)
    pen.right(90)
    pen.forward(60)
    pen.right(90)
pen.end_fill()
pen.penup()
pen.goto(-150,40)
pen.pendown()
pen.fillcolor('white')
pen.begin_fill()
for i in range(2):
    pen.forward(300)
    pen.right(90)
    pen.forward(60)
    pen.right(90)
pen.end_fill()
pen.penup()
pen.goto(-150,-20)
pen.pendown()
pen.fillcolor('green')
pen.begin_fill()
for i in range(2):
    pen.forward(300)
    pen.right(90)
    pen.forward(60)
    pen.right(90)
pen.end_fill()


pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.pencolor("blue")
pen.circle(30)
pen.penup()
pen.goto(0,10)
pen.pendown()
for i in range(24):
    pen.forward(30)
    pen.backward(30)
    pen.right(15)
turtle.done()