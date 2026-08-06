import turtle
pen = turtle.Turtle()
pen.pensize(3)
# pen.color('Orange')
# Q1 50 pixels ka square banao.
# pen.forward(50)
# pen.right(90)
# pen.forward(50)
# pen.right(90)
# pen.forward(50)
# pen.right(90)
# pen.forward(50)
# pen.right(90)

# for i in range(4):
#     pen.forward(50)
#     pen.right(90)

# Q2 300 × 150 ka rectangle banao.   
# for i in range(2):
#     pen.forward(300)
#     pen.right(90) 
#     pen.forward(150)
#     pen.right(90) 


# Q3 150 side ka triangle banao.
# for i in range(3):
#     pen.forward(150)
#     pen.left(120)

# Q4 100 radius ka circle banao.
# pen.circle(100)

# Q5 Ek square banao aur uska color blue kar do.
pen.pensize(10)
pen.pencolor('green')
pen.fillcolor('blue')
pen.begin_fill()
for i in range(4):
    pen.forward(100)
    pen.right(90)
pen.end_fill()    
turtle.done()