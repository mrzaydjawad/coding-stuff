WIDTH, HEIGHT = 1000, 1000
TITLE = "2 player game"
import pygame
import sys
import random
#pygame initialization
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#Player Classes
class Player:
    def __init__(self, x, y):
        self.x = int(520)
        self.y = int(540)
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
    
    def draw(self, win):
        pygame.draw.rect((win), self.color, self.rect)
    
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY

        #adding borders
        if self.x >= 950:
            self.x = 950
        if self.x <= 50:
            self.x = 50
        if self.y >= 950:
            self.y = 950
        if self.y <= 50:
            self.y = 50

        self.rect = pygame.Rect(int(self.x), int(self.y), 25, 25)

player = Player(WIDTH/2, HEIGHT/2)

class Player_2:
    def __init__(self, x_2, y_2):
        self.x_2 = int(420)
        self.y_2 = int(540)
        self.rect_2 = pygame.Rect(self.x_2, self.y_2, 30, 30)
        self.color_2 = (250, 120, 60)
        self.velX_2 = 0
        self.velY_2 = 0
        self.left_pressed_2 = False
        self.right_pressed_2 = False
        self.up_pressed_2 = False
        self.down_pressed_2 = False
        self.speed_2 = 4
    
    def draw(self, win):
        pygame.draw.rect(win, self.color_2, self.rect_2)
    
    def update(self):
        self.velX_2 = 0
        self.velY_2 = 0
        if self.left_pressed_2 and not self.right_pressed_2:
            self.velX_2 = -self.speed_2
        if self.right_pressed_2 and not self.left_pressed_2:
            self.velX_2 = self.speed_2
        if self.up_pressed_2 and not self.down_pressed_2:
            self.velY_2 = -self.speed_2
        if self.down_pressed_2 and not self.up_pressed_2:
            self.velY_2 = self.speed_2
        
        self.x_2 += self.velX_2
        self.y_2 += self.velY_2

        #adding borders
        if self.x_2 >= 950:
            self.x_2 = 950
        if self.x_2 <= 50:
            self.x_2 = 50
        if self.y_2 >= 950:
            self.y_2 = 950
        if self.y_2 <= 50:
            self.y_2 = 50

        self.rect_2 = pygame.Rect(int(self.x_2), int(self.y_2), 25, 25)

player_2 = Player_2(WIDTH/2, HEIGHT/2)

#obstacles

class Obstacle:
    def __init__(self_3, x_3, y_3):
        self_3.x_3 = int(0)
        self_3.y_3 = int(800)
        self_3.rect_3 = pygame.Rect(self_3.x_3, self_3.y_3, 500, 30)
        self_3.color_3 = (179, 0, 0)
        self_3.velX_3 = 0
        self_3.velY_3 = 2
        self_3.speed_3 = 4
        
    def draw(self_3, win):
        pygame.draw.rect((win), self_3.color_3, self_3.rect_3)
    
    def update(self_3):
        self_3.velX_3 = 0
        self_3.velY_3 = 0
        
        self_3.rect_3 = pygame.Rect(int(self_3.x_3), int(self_3.y_3),1000, 50)

obstacle = Obstacle(WIDTH/2, HEIGHT/2)

#Main Loop

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            #player 1 controls

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

            #player 2 controls

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_2.left_pressed_2 = True
            if event.key == pygame.K_d:
                player_2.right_pressed_2 = True
            if event.key == pygame.K_w:
                player_2.up_pressed_2 = True
            if event.key == pygame.K_s:
                player_2.down_pressed_2 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_2.left_pressed_2 = False
            if event.key == pygame.K_d:
                player_2.right_pressed_2 = False
            if event.key == pygame.K_w:
                player_2.up_pressed_2 = False
            if event.key == pygame.K_s:
                player_2.down_pressed_2 = False  

    obstacle 
    
    #Draw

    win.fill((12, 24, 36))  
    player.draw(win)
    player_2.draw(win)
    obstacle.draw(win)

    #update

    player.update()
    player_2.update()
    obstacle.update()
    pygame.display.flip()

    clock.tick(120)