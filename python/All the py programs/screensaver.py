import time
import pygame as py
py.init()
screen = py.display.set_mode((1920,1080))
bg = py.image.load('C:/Users/zaydz/Desktop/coding/python/All the py programs/images/space.png')
mover = py.image.load('C:/Users/zaydz/Desktop/coding/python/All the py programs/images/waterbottles.png')
clock = py.time.Clock()
tick = 30
running = True
while running:
    screen.blit(bg,(0,0))
    screen.blit(mover,(890,490))
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
