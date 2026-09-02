import turtle
pen  = turtle.Turtle()



# def move():
#     pen.forward(50)
# turtle.ontimer(move,2000)




# 3. Ab important part: baar-baar chalana
# Agar hume turtle ko continuously move karna hai:
# def move_F():
#     pen.forward(50)
#     turtle.ontimer(move_F,1000)
# move_F()    




# 6. Animation example 🎨
def rotate():
    pen.right(30)
    turtle.ontimer(rotate,1000)
rotate()    
turtle.done()