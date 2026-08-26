import turtle
pen = turtle.Turtle()
# def move():
#     pen.forward(10)
# def stop():
#     print('Up Key Released')  
pen.shape('turtle')
def game_loop():
    pen.penup()
    pen.forward(10)
    turtle.ontimer(game_loop,500)
game_loop()
turtle.listen()
# turtle.onkeypress(move,'Up')
# turtle.onkeyrelease(stop,'Up')      

turtle.done()

# import turtle

# pen = turtle.Turtle()

# moving = False

# def move():
#     global moving
#     moving = True
#     print('Move',moving)

# def stop():
#     global moving
#     moving = False
#     print('stop ',moving)

# def game_loop():
#     print('Game loop',moving)
#     if moving:
#         pen.forward(5)

#     turtle.ontimer(game_loop, 1000)

# turtle.listen()

# turtle.onkeypress(move, "Up")
# turtle.onkeyrelease(stop, "Up")

# game_loop()

# turtle.done()


# import turtle

# pen = turtle.Turtle()

# def game_loop():
#     pen.forward(5)
#     turtle.ontimer(game_loop, 500)

# game_loop()

# turtle.done()