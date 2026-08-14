import turtle
pen = turtle.Turtle()
pen.color('orange')
pen.width(5)
# q1 50pixels ka square bnao
# for i in range(4):
#     pen.forward(50)
#     pen.right(90)


# q2 :300*150 ka reactangel bnao
# for i in range(2):
#     pen.forward(300)
#     pen.right(90)
#     pen.forward(150)
#     pen.right(90)

# q3 : 150 side ka triange bnao
# for i in range(3):
#     pen.forward(150)
#     pen.left(120)

# q4 100 radius ka circle bnao
# pen.circle(100)

# q5 ek square bnao uska color blue kr do
pen.fillcolor('blue')
pen.begin_fill()
for i in range(4):
    pen.forward(150)
    pen.right(90)
pen.end_fill()    
turtle.done()