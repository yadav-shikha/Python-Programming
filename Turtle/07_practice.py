import turtle
pen = turtle.Turtle()
# Q1 Turtle ko har 1 second me 20 pixels forward move karna hai.
# def move():
#     pen.forward(20)
#     turtle.ontimer(move,1000)
# move()    



# Q2 Turtle ko har 100 milliseconds me 5° right rotate karna hai.
# def rotate():
#     pen.right(5)
#     turtle.ontimer(rotate,100)
# rotate()


# Q3 ⭐ Turtle ko continuously square draw karvao.
side = 0
def square():
    global side

    if side < 4:
        pen.forward(100)
        pen.right(90)
        side += 1

        turtle.ontimer(square, 1000)
square() 
turtle.done()