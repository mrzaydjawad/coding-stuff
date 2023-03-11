import turtle
import random 
r_x = random.randint(0,1500)
r_y = random.randint(0,1000)
win = turtle.Screen()
win.title("moving")
win.bgcolor("green")
win.setup(width=1500, height=1000)
win.tracer(0)
def food():
    f = turtle.Turtle()
    f.speed(0)
    f.shape("square")
    f.penup()
    f.goto(r_x,r_y)
def importantmoving():
    #moving
    a = turtle.Turtle()
    a.speed(0)
    a.shape("square")
    a.color("white")
    a.penup()
    a.goto(0,0)
    #functions
    def a_up():
        y = a.ycor()
        y += 20
        a.sety(y)
    def a_down():
        y = a.ycor()
        y -= 20
        a.sety(y)
    def a_right():
        x = a.xcor()
        x += 20
        a.setx(x)
    def a_left():
        x = a.xcor()
        x -= 20
        a.setx(x)
    #keyboard binding
    win.listen()
    win.onkeypress(a_up,"Up")
    win.onkeypress(a_right,"Right")
    win.onkeypress(a_down,"Down")
    win.onkeypress(a_left,"Left")
while True:
    win.update()
    importantmoving()
    food()