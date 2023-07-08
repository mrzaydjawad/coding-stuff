import pygame
import datetime
pygame.init()
#defining all the variables
screen = pygame.display.set_mode((1920,1080))
bg = pygame.image.load('E:\coding and wor\coding\python\python programs\images\wpfff.jpg')
miliseconds = 0
seconds = 0
minutes = 0
hours = 0
date_time_1 = datetime.datetime.now()
start_date_time = date_time_1.strftime("%Y/%m/%d,%H:%M:%S")
clock = pygame.time.Clock()
#making a clock
def clock_run():
    global miliseconds,seconds,minutes,hours
    miliseconds += 1
    if miliseconds == 50:
        seconds += 1
        miliseconds -= 50
    if seconds == 60:
        minutes += 1
        seconds -= 60 
    if minutes == 60:
        hours += 1
        minutes -= 60
    if hours == 24:
        seconds = 0
        minutes = 0
        hours = 0
        miliseconds = 0 
def date_time():
    global current_date_time,date,time
    current_date_time = datetime.datetime.now()
    date = current_date_time.strftime("%Y/%m/%d")
    time = current_date_time.strftime("%H:%M:%S")
running = True
#making the loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    date_time()
    clock_run()
    #background 
    screen.blit(bg,(0,0))
    #displaying the start time
    start_date_time_font = pygame.font.Font("E:/coding and wor/coding/python/python programs/fonts/arial.ttf",50)
    start_date_time_render = start_date_time_font.render(f"start time is {start_date_time}",False,(255,255,255))
    screen.blit(start_date_time_render,(0,300))
    #displaying current date and time on the screen
    date_time_font = pygame.font.Font("E:/coding and wor/coding/python/python programs/fonts/arial.ttf",50)
    date_render = date_time_font.render((date),False,(255,255,255))
    time_render = date_time_font.render((time),False,(255,255,255))
    screen.blit(time_render,(0,100))
    screen.blit(date_render,(0,200))
    #displaying clock on the screen
    clock_font = pygame.font.Font("E:/coding and wor/coding/python/python programs/fonts/arial.ttf",50)
    clock_render = clock_font.render(f"hour : {hours}  minute : {minutes}  second : {seconds}",False,(255,255,255))
    screen.blit(clock_render,(0,0))
    #update
    pygame.display.update()
    clock.tick(50)