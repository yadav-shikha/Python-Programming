import turtle
pen = turtle.Turtle()
# 1. goto(x, y) goto() turtle ko screen ke kisi bhi coordinate par le jata hai.
# pen.goto(100,100)
# pen.goto(-100,100)
# pen.goto(-100,-100)
# pen.goto(100,-100)

# 2. setheading(angle)
# Ye turtle ki direction set karta hai.
# Directions
# Angle	Direction
# 0	Right →
# 90	Up ↑
# 180	Left ←
# 270	Down ↓
# pen.setheading(90)
# pen.setheading(0)
# pen.setheading(180)
# pen.setheading(270)
# pen.forward(100)

# 3. dot() Screen par ek dot banata hai.
# pen.dot(30)
# pen.dot(40,'red')

# 4. write() Screen par text likhne ke liye.
# pen.write('Helo shikha')
# pen.write('Helo Shikha',font= ('Arial',20,'bold'))

# Ye turtle ka current shape screen par print kar deta hai.
# pen.stamp()
# pen.forward(100)
# pen.stamp()
# pen.forward(100)
# pen.stamp()
# pen.forward(100)

# star
# 144° kyun? Star me 5 points hote hain. Is shape ke liye mathematically 144° turn use hota hai.
for i in range(5):
    pen.forward(150)
    pen.right(144)


# Hexagon  6 sides   360 ÷ 6 = 60°
for i in range(6):
    pen.forward(150)
    pen.right(60)    


# Spiral

# colors = ['red','green','blue','yellow','purple','orange']
# pen.speed(0)
# for i in range(100):

#     pen.pencolor(colors[i % 6])

#     pen.forward(i*4)

#     pen.right(91)
turtle.done()