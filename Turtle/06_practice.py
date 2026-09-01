# level 1
# import turtle
# pen = turtle.Turtle()
# screen = turtle.Screen()
# Q1.Keyboard se Turtle control karo:
# Up → 20 pixels forward
# Down → 20 pixels backward

# def move_forward():
#     pen.forward(20)
# def move_backward():
#     pen.backward(20)    

# Q2.Keyboard se Turtle ko rotate karo:
# Left → 15° left
# Right → 15° right
# def rotate_left():
#     pen.left(15)
# def rotate_right():
#     pen.right(15)

# Q3.Space press karne par Turtle ka pen color "red" ho jaye.
# def color_change():
#     pen.color('red')

# Q4. b press karne par Turtle ka pen color "blue" ho jaye.
# def color_blue():
#     pen.color('blue')

# turtle.listen()
# turtle.onkey(move_forward,'Up')   
# turtle.onkey(move_backward,'Down')
# turtle.onkey(rotate_left,'Left')
# turtle.onkey(rotate_right,'Right')
# turtle.onkey(color_change,'space')
# turtle.onkey(color_blue,'b')
# turtle.done()




# 🟡 Level 2 — Combine Concepts
import turtle
import random
pen = turtle.Turtle()

# Q5.Ek program banao jisme:
# Up → forward 20
# Down → backward 20
# Left → left 15°
# Right → right 15°
# r → red pen
# g → green pen
# b → blue pen
def control(action):
    if action =='forward':
        pen.forward(20)
    elif action =='backward':
        pen.backward(20)    
    elif action =='left':
        pen.left(15)
    elif action =='right':
        pen.right(15)
    elif action == 'red':
        pen.color('red')   
    elif action == 'blue':
        pen.color('blue') 
    elif action == 'green':
        pen.color('green') 



# Q6.Mouse screen par click karne par Turtle clicked position par jaye aur 20 size ka red dot banaye.
# def clicked(x,y):
#     pen.goto(x,y)
#     pen.dot(20,'red')


# Q7.Mouse par click karne par clicked location par random color ka dot bane.
color = ['red','green','blue','orange','purple','yellow','skyblue']
def dots(x,y):
    pen.goto(x,y)
    pen.dot(20,random.choice(color))
    
# Q8. ⭐Keyboard se Turtle ko move karte hue apna naam karne ki koshish karo.
    pen.write('Shikha yadav')
# Q9. ⭐Space press karne par Turtle circle banaye:
def space_press():
    pen.circle(80)
# Q10. ⭐Enter press karne par Turtle ek square banaye.
def square():
    for i in range(4):
        pen.forward(50)
        pen.right(90)
turtle.listen()
# turtle.onscreenclick(clicked)
turtle.onkey(lambda : control('forward'),'Up')
turtle.onkey(lambda : control('backward'),'Down')
turtle.onkey(lambda : control('left'),'Left')
turtle.onkey(lambda : control('right'),'Right')
turtle.onkey(lambda : control('red'),'r')
turtle.onkey(lambda : control('green'),'g')
turtle.onkey(lambda : control('blue'),'b')
turtle.onscreenclick(dots)
turtle.onkeypress(space_press,'space')
turtle.onkeypress(square,'Return')
turtle.done()
