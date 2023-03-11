import random
import pygame
pygame.init()
#defining all the variables
screen = pygame.display.set_mode((1920,1080))
bg = pygame.image.load('C:/Users/zaydz/Desktop/coding/python/python programs/images/backrooms.jpg')
mover = pygame.image.load('C:/Users/zaydz/Desktop/coding/python/python programs/images/welcome.png')
miliseconds = 0
seconds = 0
minutes = 0
hours = 0
left_wall = 0
right_wall = 0
up_wall = 0
down_wall = 0
corner = 0
mx = random.randrange(400,1520)
my = random.randrange(200,880)
sx = 3
sy = 2
clock = pygame.time.Clock()
#making the clock
def time_run():
    global miliseconds,seconds,minutes,hours
    miliseconds += 1
    if miliseconds > 50:
        seconds += 1
        miliseconds -= 50
    if seconds > 60:
        minutes += 1
        seconds -= 60 
    if minutes > 60:
        hours += 1
        minutes -= 60
    if hours > 24:
        seconds = 0
        minutes = 0
        hours = 0
        miliseconds = 0 
running = True
#making the game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    time_run()
    time = (miliseconds,seconds,minutes,hours)
    #randomize the position of the moving box
    mx += sx
    my += sy
    #add borders
    if mx <= 0 or mx >= 1520:
        sx *= -1
    if my <=0 or my >= 880:
        sy *= -1
    #checking for wall collisions
    if mx <= 0:
        left_wall += 1
    if mx >= 1520:
        right_wall += 1
    if my <= 0:
        up_wall += 1
    if my >= 880:
        down_wall += 1
    #checking for corners
    if (mx >= 1520) and (my >= 880):
        corner += 1
    if (mx >= 1520) and (my <= 0):
        corner += 1
    if (mx <= 0) and (my >= 880):
        corner += 1
    if (mx <= 0) and (my <= 0):
        corner += 1
    #putting everything on the screen
    tume = pygame.font.Font("C:/Users/zaydz/Desktop/coding/python/python programs/fonts/Sitka.ttc",50)
    tumo = tume.render(f"hour : {hours}  minute : {minutes}  second : {seconds}",False,(255,255,255))
    wallas = pygame.font.Font("C:/Users/zaydz/Desktop/coding/python/python programs/fonts/Sitka.ttc",50)
    walls = wallas.render(f"left wall:{left_wall}  right wall:{right_wall}  upper wall:{up_wall}  lower wall:{down_wall}  corners:{corner}",False,(255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(mover,(mx,my))
    screen.blit(tumo,(570,0))
    screen.blit(walls,(0,1030))
    pygame.display.update()
    clock.tick(50)