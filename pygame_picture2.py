import numpy as np

import pygame
from pygame.draw import *



pygame.init()

FPS = 30
screen = pygame.display.set_mode((1800, 900))

screen.fill((0, 250, 250))

#ground
rect(screen, (0, 204, 0), (0, 450, 1800, 450))

def picture(x,y,s): #house with tree

    #house
    rect(screen, (0, 0, 0), (x+np.int(s*317), y+np.int(s*297), np.int(s*356), np.int(s*256)))
    rect(screen, (204, 102, 0), (x+np.int(s*320), y+np.int(s*300), np.int(s*350), np.int(s*250)))

    #roof
    polygon(screen, (0, 0, 0), [(x+np.int(s*283), y+np.int(s*300)), (x+np.int(s*(317 + 27 + 356 + 7)), y+np.int(s*300)), (x+np.int(s*((290 + 317 + 27 + 356)/2)), y+np.int(s*115))])
    polygon(screen, (255, 153, 51), [(x+np.int(s*290), y+np.int(s*297)), (x+np.int(s*(317 + 27 + 356)), y+np.int(s*297)), (x+np.int(s*((290 + 317 + 27 + 356)/2)), y+np.int(s*120))])

    #window
    rect(screen, (153, 153, 9), (x+np.int(s*420), y+np.int(s*360), np.int(s*80), np.int(s*100)))
    rect(screen, (0, 76, 153), (x+np.int(s*425), y+np.int(s*365), np.int(s*70), np.int(s*90)))

    #tree
    rect(screen, (0, 0, 0), (x+s*1300, y+s*300, s*40, s*220))

    circle(screen, (0, 0, 0), (x+np.int(s*1320), y+np.int(s*100)), np.int(s*74))
    circle(screen, (0, 102, 51), (x+np.int(s*1320), y+np.int(s*100)), np.int(s*70))

    circle(screen, (0, 0, 0), (x+np.int(s*1250), y+np.int(s*150)), np.int(s*74))
    circle(screen, (0, 102, 51), (x+np.int(s*1250), y+np.int(s*150)), np.int(s*70))

    circle(screen, (0, 0, 0), (x+np.int(s*1370), y+np.int(s*190)), np.int(s*74))
    circle(screen, (0, 102, 51), (x+np.int(s*1370), y+np.int(s*190)), np.int(s*70))

    circle(screen, (0, 0, 0), (x+np.int(s*1320), y+np.int(s*260)), np.int(s*74))
    circle(screen, (0, 102, 51), (x+np.int(s*1320), y+np.int(s*260)), np.int(s*70))

    circle(screen, (0, 0, 0), (x+np.int(s*1390), y+np.int(s*310)), np.int(s*74))
    circle(screen, (0, 102, 51), (x+np.int(s*1390), y+np.int(s*310)), np.int(s*70))

    circle(screen, (0, 0, 0), (x+np.int(s*1240), y+np.int(s*250)), np.int(s*74))
    circle(screen, (0, 102, 51), (x+np.int(s*1240), y+np.int(s*250)), np.int(s*70))

    circle(screen, (0, 0, 0), (x+np.int(s*1270), y+np.int(s*300)), np.int(s*74))
    circle(screen, (0, 102, 51), (x+np.int(s*1270), y+np.int(s*300)), np.int(s*70))




#cloud

def cloud(x,y):
    circle(screen, (0, 0, 0), (x+800, y+150), 63)
    circle(screen, (251, 251, 251), (x+800, y+150), 60)

    circle(screen, (0, 0, 0), (x+850, y+150), 63)
    circle(screen, (251, 251, 251), (x+850, y+150), 60)

    circle(screen, (0, 0, 0), (x+920, y+160), 63)
    circle(screen, (251, 251, 251), (x+920, y+160), 60)

    circle(screen, (0, 0, 0), (x+990, y+150), 63)
    circle(screen, (251, 251, 251), (x+990, y+150), 60)

    circle(screen, (0, 0, 0), (x+950, y+120), 63)
    circle(screen, (251, 251, 251), (x+950, y+120), 60)

    circle(screen, (0, 0, 0), (x+870, y+100), 63)
    circle(screen, (251, 251, 251), (x+870, y+100), 60)


picture(200,400,0.5)
picture(400,600,0.5)
picture(800,200,0.6)

cloud(0,0)
cloud(-400,100)
cloud(400,-50)
#sun

n = 18   #spikes
for theta in range(0, n, 1):
    t = 2*(3.141560) /n

    x = 1590 + 50*np.cos(t*theta)
    y = 100 + 50*np.sin(t*theta)

    x1 = 1590 + 50*np.cos(t*(theta+1))
    y1 = 100 + 50*np.sin(t*(theta+1))

    x2 = 1590 + 60*np.cos(t*(theta+0.5))
    y2 = 100 + 60*np.sin(t*(theta+0.5))

    polygon(screen, (204, 204, 0), [(x,y), (x1,y1), (x2,y2)])

circle(screen, (255, 255, 0), (1590, 100), 50)

pygame.display.update()

finished = False

clock = pygame.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
