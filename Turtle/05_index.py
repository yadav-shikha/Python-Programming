import turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(3)
def move():
    pen.forward(100)

def move_up():
    pen.setheading(90)
    pen.forward(20)
def move_down():
    pen.setheading(270)
    pen.forward(20)
def move_right():
    pen.setheading(0)
    pen.forward(20)
def move_left():
    pen.setheading(180)
    pen.forward(20)        
screen.onkey(move,'space')   
screen.onkey(move_up,'Up')
screen.onkey(move_down,'Down')
screen.onkey(move_left,'Left')
screen.onkey(move_right,'Right') 
# 12. Keyboard se Color Change 🎨
def make_red():
    pen.color('red')
def make_blue():
    pen.color('blue')   

screen.onkey(make_red,'r')
screen.onkey(make_blue,'b')    

# 13. Keyboard se Pen Up / Down
def pen_up():
    pen.penup()
def pen_down():
    pen.pendown()  


# 14. Mouse Click Event 🖱️
screen.onkey(pen_up,'u')
screen.onkey(pen_down,'d')  


# def click(x, y):
#     pen.goto(x, y)

# turtle.onscreenclick(click)

screen.listen()
turtle.done()