import turtle

screen = turtle.Screen()

# =========================
# GitHub code
# =========================

screen.bgcolor('orange')

pen = turtle.Turtle()
pen.shape('turtle')
pen.speed(1)

pen.fillcolor('blue')
pen.begin_fill()
pen.circle(80)
pen.end_fill()


# =========================
# Local code - Turtle practice
# =========================

# shape
# pen.shape('classic')
# pen.forward(100)

# speed()
# pen.speed(1)

# fill color
# pen.fillcolor('red')
# pen.begin_fill()
# for i in range(5):
#     pen.forward(150)
#     pen.right(144)
# pen.end_fill()

# pen size
# pen.width(5)
# pen.pensize(5)

# hideturtle
# pen.hideturtle()

# pen.home()
# pen.clear()


# random color drawing
# import random
# colors = ['red','green','yellow','blue','purple','orange','cyan']
# for i in range(30):
#     pen.pencolor(random.choice(colors))
#     pen.forward(100)
#     pen.right(170)


# screen title
# screen.title('Shikha turtle program')


# =========================
# Local code - Lesson 5
# Mouse Event
# =========================


turtle.done()