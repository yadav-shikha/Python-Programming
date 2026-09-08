import turtle
pen = turtle.Turtle()
# Q1 Turtle ko 100 pixels forward move karo aur phir uski current x aur y position print karo.
pen.forward(100)
print(pen.xcor())
print(pen.ycor())

# def move():
#     pen.forward(10)
#     if pen.xcor() > 100:
#         turtle.ontimer(move,1000)
# move()

# Q2 Turtle ko ontimer() se har 100 ms me 10 pixels forward move karao.
# Lekin condition lagao:
# Jab Turtle ki x position 200 se zyada ho jaye, movement stop ho jaye.
# def move():
#     pen.forward(10)
#     if pen.xcor()< 200:
#         turtle.ontimer(move,50)
# move()

# Q3 Turtle ko continuously forward move karao.
# Jab Turtle ki x position 200 cross kare, to use automatically:
# pen.goto(-200, 0)
# par le jao.
# Phir movement dobara continue hona chahiye.

def moveForward():
    pen.forward(10)
    if pen.xcor() <200:
        turtle.ontimer(moveForward,50)
    else:
        pen.goto(-200,0)
        turtle.ontimer(moveForward,50)

turtle.done()