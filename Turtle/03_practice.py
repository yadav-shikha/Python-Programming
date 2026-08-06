import turtle
pen = turtle.Turtle()
pen.color('lime')
pen.pensize(3)
# Q1 goto() ki help se square ke 4 corners par jao.
# pen.goto(100,100)
# pen.goto(-100,100)
# pen.goto(-100,-100)
# pen.goto(100,-100)

# Q2 4 alag-alag jagah red dot banao.
# pen.goto(100,100)
# pen.dot(20,'red')
# pen.goto(-100,100)
# pen.dot(20,'red')
# pen.goto(-100,-100)
# pen.dot(20,'red')
# pen.goto(100,-100)
# pen.dot(20,'red')

# Q3 Apna naam screen par likho.
# pen.write('Shikha Yadav')


# Q4 Hexagon banao.
# for i in range(6):
#     pen.forward(150)
#     pen.right(60)

# Q5 Star banao.    
# for i in range(5):
#     pen.forward(150)
#     pen.right(144)

# Q6 (Challenge ⭐)

# Ek hi program me:

# Ek blue square
# Uske right me red circle
# Uske niche green star

# Banane ki koshish karo. Isse penup(), goto() aur alag-alag shapes ka practice ho jayega.
pen.fillcolor('blue')
pen.begin_fill()
for i in range(4):
    pen.forward(100)
    pen.right(90)
pen.end_fill()    

pen.penup()
pen.goto(200,0)
pen.pendown()
pen.color('red')
pen.circle(80)
pen.color('orange')
pen.penup()
pen.goto(0,-200)
pen.pendown()
for i in range(5):
    pen.forward(150)
    pen.right(144)


# pen.penup()

# pen.goto(50, 50)

# pen.goto(150, 50)

# pen.goto(150, -50)

# pen.goto(50, -50)
turtle.done()