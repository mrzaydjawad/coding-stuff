import random
import pygame
import time
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1920,1080))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
    pygame.display.update()
    clock.tick(50)
