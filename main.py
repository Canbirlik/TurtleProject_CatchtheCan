# import for turtle
import turtle

# Starting a Working Screen
ws = turtle.Screen()
ws.bgcolor("cyan")
ws.title("Turtle Team")

# initializing a turtle instance
geekyTurtle = turtle.Turtle()
geekyTurtle.color("green")

'''
# executing loop 5 times for a star
def star_turtle(size):
    for i in range(5):
        # moving turtle 100 units forward
        geekyTurtle.forward(size)

        # rotating turtle 144 degree right
        geekyTurtle.right(144)

star_turtle(100)
'''

'''
geekyColors = ["blue", "green", "yellow", "red", "black", "orange"]
for i in range(10):
    geekyTurtle.color(geekyColors[i % 6])
    geekyTurtle.circle(10 * i)
    geekyTurtle.circle(-10 * i)
'''

def turtle_space():
    geekyTurtle.forward(50)

def turtle_angle_right():
    geekyTurtle.right(30)

def turtle_angle_left():
    geekyTurtle.left(30)

def turtle_clear():
    geekyTurtle.clear()

def turtle_home():
    geekyTurtle.penup()
    geekyTurtle.home()
    geekyTurtle.pendown()

def turtle_pen_up():
    geekyTurtle.penup()

def turtle_pen_down():
    geekyTurtle.pendown()

ws.listen()
ws.onkey(fun=turtle_space,key="space")
ws.onkey(fun=turtle_clear,key="c")
ws.onkey(fun=turtle_home,key="h")
ws.onkey(fun=turtle_pen_up,key="w")
ws.onkey(fun=turtle_pen_down,key="q")
ws.onkey(fun=turtle_angle_right,key="Down")
ws.onkey(fun=turtle_angle_left,key="Up")

# Completing Turtle and not closing the window
# turtle.done()
turtle.mainloop()