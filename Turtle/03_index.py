import turtle
pen = turtle.Turtle()
# goto
# pen.goto(100,100)

#setheading 
# pen.setheading(270)
# pen.forward(120)

# dot()
# pen.dot()
# pen.dot(30,'red')

# write()
# pen.write('Hello world')
# pen.write('Hello shikha',font=("Arial",20,'bold'))

# stamp
# pen.shape('turtle')
# pen.stamp()
# pen.forward(100)
# pen.stamp()
# pen.forward(100)
# pen.stamp()

# star 
# for i in range(5):
#     pen.forward(150)
#     pen.right(144)

# hexagon
# for i in range(6):
#     pen.forward(100)
#     pen.right(60)

# spiral
# for i in range(100):
#     pen.forward(i*5)
#     pen.right(50)

colors = ['red','blue','green','yellow','purple','orange','black']
for i in range(100):
    pen.pencolor(colors[i%6])
    pen.forward(i*4)
    pen.right(91)
turtle.done()