import random
import pygame as py
py.init()
screen = py.display.set_mode((1920,1080))
bg = py.image.load('C:/Users/zaydz/Desktop/coding/python/python programs/images/backrooms.jpg')
mover = py.image.load('C:/Users/zaydz/Desktop/coding/python/python programs/images/welcome.png')
mx = random.randrange(400,1520)
my = random.randrange(200,880)
sx = 3
sy = 2
clock = py.time.Clock()
tick = 30
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.blit(bg,(0,0))
    screen.blit(mover,(mx,my))
    py.display.update()
    mx += sx
    my += sy
    if mx <= 0 or mx >= 1520:
        sx *= -1
    if my <=0 or my >= 880:
        sy *= -1