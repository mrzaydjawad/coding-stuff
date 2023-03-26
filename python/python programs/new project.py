import pygame
pygame.init()
screen = pygame.display.set_mode((1408,792))
block = pygame.image.load('C:/Users/zaydz/Pictures/pcc2.jpg')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(block,(0,0))
    
    pygame.display.update()