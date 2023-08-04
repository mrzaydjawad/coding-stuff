import turtle
import colorsys
win = turtle.Screen()
win.title("hmmmm")
win.bgcolor("black")
win.setup(width=1920, height=1080)
win.tracer(0)
def one():
    a = turtle.Turtle()
    cc = 0
    for i in range(1000):
        color = colorsys.hsv_to_rgb(cc,1,0.5)
        cc += 1/70
        a.color(color)
        a.forward(100)
        a.left(250)
        for j in range(20):
            a.forward(100)
            for k in range(4):
                a.forward(25)
                a.right(250)
def two():
    b = turtle.Turtle()
    ll = 100
    ff = 100
    cc = 0
    for i in range(50):
        color = colorsys.hsv_to_rgb(cc,1,0.5)
        cc += 1/70
        b.color(color)
        for f in range(100):
            ff -= 0.1
            b.forward(ff)
            ll += 10
            b.left(ll)
            print(ll)
def menu():
    print("[1]\n[2]")
    d = int(input("slect an animation thing(1,2):"))
    if d == 1:
        one()
    if d == 2:
        two()
menu()
while True:
    win.update()