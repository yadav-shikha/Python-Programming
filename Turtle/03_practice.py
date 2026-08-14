import turtle
pen = turtle.Turtle()
# goto ki help se square k 4 corners par jao
# pen.goto(100,100)
# pen.goto(-100,100)
# pen.goto(-100,-100)
# pen.goto(100,-100)

# q2 4 alag alag jagah red dot bnao
# pen.goto(100,100)
# pen.dot(40,'red')
# pen.goto(-100,100)
# pen.dot(40,'red')
# pen.goto(-100,-100)
# pen.dot(40,'red')
# pen.goto(100,-100)
# pen.dot(40,'red')


# apna name screen par likho
pen.write('Shika yadav')

# hexagon bnao
# for i in range(6):
#     pen.forward(100)
#     pen.right(60)

# star bnao
for i in range(5):
    pen.forward(150)
    pen.right(144)
turtle.done()