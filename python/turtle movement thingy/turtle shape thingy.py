import turtle

def importantmoving():
    win = turtle.Screen()
    win.title("moving")
    win.bgcolor("black")
    win.setup(width=1920, height=1080)
    win.bgpic('bg.gif')
    win.tracer(0)
    #moving
    a = turtle.Turtle()
    a.speed(1)
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
        #border
        if a.ycor()<-800:
            a.sety(-795)
        if a.ycor()>800:
            a.sety(795)
        if a.xcor()<-800:
            a.setx(-795)
        if a.xcor()>800:
            a.setx(795)


importantmoving()