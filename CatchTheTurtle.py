# import turtle & random
import turtle
from random import randint

# Starting a Screen
cbScreen = turtle.Screen()
cbScreen.bgcolor("white")
cbScreen.title("Catch the Can")

# Other Setups
game_over = False
time = 10
max_time = 10
style = ('Courier', 30, 'bold')
top_height = cbScreen.window_height()
top_width = cbScreen.window_width()
score = 0
turtle.register_shape("barbar.gif")
turtle.register_shape("cb.gif")

# Score & Barbar turtle instances
scoreTurtle = turtle.Turtle()
diabloTurtle = turtle.Turtle()
timerTurtle = turtle.Turtle()

def barbar_hide():
    diabloTurtle.hideturtle()
    diabloTurtle.penup()
    diabloTurtle.home()
    diabloTurtle.goto(randint(int(-1 * (top_width / 2)), int(top_width / 2)), randint(int(-1 * (top_height / 2) * 0.80), int((top_height / 2) * 0.60)))
    diabloTurtle.showturtle()

# Setup Score turtle
def setup_score_turtle():
    scoreTurtle.color("green")
    scoreTurtle.hideturtle()
    scoreTurtle.penup()
    scoreTurtle.setpos(0, (top_height / 2) * 0.70)
    scoreTurtle.write(f'Score: {score}', font=style, align='center')

# Setup Timer turtle
def setup_timer_turtle():
    timerTurtle.color("red")
    timerTurtle.hideturtle()
    timerTurtle.penup()
    timerTurtle.setpos(0, (top_height / 2) * 0.85)
    timerTurtle.write(f"Time Left: {time}", font=style, align='center')

# Setup Barbar turtle
def setup_barbar_turtle():
    global game_over
    diabloTurtle.shape("cb.gif")
    if game_over:
        diabloTurtle.hideturtle()
    if not game_over:
        diabloTurtle.onclick(fun=barbar_score, btn=1)
        barbar_hide()
        cbScreen.ontimer(setup_barbar_turtle, 500)

def countdown(time):
    global game_over
    if time > 0:
        timerTurtle.clear()
        timerTurtle.write(f"Time Left: {time}", font=style, align='center')
        cbScreen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        diabloTurtle.hideturtle()
        timerTurtle.clear()
        timerTurtle.write("Game Over", font=style, align='center')

def barbar_score(x,y):
    global score
    score += 1
    scoreTurtle.clear()
    scoreTurtle.write(f'Score: {score}', font=style, align='center')

def game_setup():
    turtle.tracer(0)
    setup_barbar_turtle()
    setup_timer_turtle()
    setup_score_turtle()
    countdown(time)
    turtle.tracer(1)

game_setup()
turtle.mainloop()