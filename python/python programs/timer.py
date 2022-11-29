import turtle
import time
win = turtle.Screen()
win.bgcolor("black")
win.setup(width = 1920,height=1080)
win.tracer(0)
seconds = 0
minutes = 0
hour = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.write((f"hour {hour}: minute {minutes}: second {seconds}"),align="center",font=("courier",50,"normal"))
while True:
    win.update()
    for i in range(60):
        seconds += 1
        time.sleep(1)
        pen.clear()
        pen.write((f"hour {hour}: minute {minutes}: second {seconds}"),align="center",font=("courier",50,"normal"))
    for i in range (60):
        if seconds == 60:
            seconds -= 60
            minutes += 1
            pen.clear()
            pen.write((f"hour {hour}: minute {minutes}: second {seconds}"),align="center",font=("courier",50,"normal"))
    for i in range(24):
         if minutes == 60:
            minutes -= 60
            hour += 1
            pen.clear()
            pen.write((f"hour {hour}: minute {minutes}: second {seconds}"),align="center",font=("courier",50,"normal"))
         if hour == 24:
            seconds -= 60
            minutes -= 60
            hour -= 24