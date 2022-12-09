import random
import pygame
pygame.init()
screen = pygame.display.set_mode((1920,1080))
bg = pygame.image.load('C:/Users/zaydz/Desktop/coding/python/python programs/images/backrooms.jpg')
mover = pygame.image.load('C:/Users/zaydz/Desktop/coding/python/python programs/images/welcome.png')
miliseconds = 0
seconds = 0
minutes = 0
hours = 0
mx = random.randrange(400,1520)
my = random.randrange(200,880)
sx = 3
sy = 2
start_time = None
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
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
    mx += sx
    my += sy
    if mx <= 0 or mx >= 1520:
        sx *= -1
    if my <=0 or my >= 880:
        sy *= -1
    tume = pygame.font.Font("C:/Users/zaydz/Desktop/coding/python/python programs/fonts/Sitka.ttc",50)
    tumo = tume.render(f"hour : {hours}  minute : {minutes}  second : {seconds}",False,(237, 205, 187))
    screen.blit(bg,(0,0))
    screen.blit(mover,(mx,my))
    screen.blit(tumo,(0,0))
    pygame.display.update()
    clock.tick(50)