import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball(x, y, r, color):
   # x = randint(100,700)
   # y = randint(100,500)
   # r = randint(30,50)
   # color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

a = 10
b = 30
def star(size, x, y, color):
    polygon(screen, color, [(x+a*size,y-a*size), (x+b*size,y), (x+a*size,y+a*size), (x,y+b*size), (x-a*size,y+a*size), (x-b*size,y), (x-a*size,y-a*size), (x, y-b*size)])

def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


points = 0
count = 0
x1 = randint(100,700)
y1 = randint(100,500)
r1 = randint(30,50)

color1 = COLORS[randint(0, 5)]

vx1 = randint(-7,7)
sign_x1 = 1
vy1 = randint(-5,5)
sign_y1 = 1

x2 = randint(100,700)
y2 = randint(100,500)
r2 = randint(30,50)

color2 = COLORS[randint(0, 5)]

vx2 = randint(-7,7)
sign_x2 = 1
vy2 = randint(-5,5)
sign_y2 = 1

x3 = randint(100,700)
y3 = randint(100,500)
size3 = randint(1,3)

color3 = COLORS[randint(0, 5)]

vx3 = randint(-7,7)
sign_x3 = 1
vy3 = randint(-5,5)
sign_y3 = 1

time_interval = 1
time = 0
    
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            count += 1
            if ((event.pos[0]-x3)**2+(event.pos[1]-y3)**2 <= b*size3*size3*b) or ((((x1-event.pos[0])**2)+((y1-event.pos[1])**2)) <= r1*r1) or ((((x2-event.pos[0])**2)+((y2-event.pos[1])**2)) <= r2*r2) :
                if ((event.pos[0]-x3)**2+(event.pos[1]-y3)**2 <= b*size3*size3*b):
                    points+=2
                    x3 = randint(100,700)
                    y3 = randint(100,500)
                points+=1
                print('Click!')

    x1 += sign_x1*vx1*time_interval
    y1 += sign_y1*vy1*time_interval

    x2 += sign_x2*vx2*time_interval
    y2 += sign_y2*vy2*time_interval

    x3 += sign_x3*vx3*time_interval*(np.sin(time)+1)
    y3 += sign_y3*vy3*time_interval*(np.cos(2*time*np.cos(time*7))-0)
    
    new_ball(x1,y1,r1,color1)
    new_ball(x2,y2,r2,color2)
    star(size3, x3, y3, color3)
    
    if (x1-1180)>20 or x1<20:
        sign_x1 *= -1
    if (y1-880)>20 or y1<20:
        sign_y1 *= -1
        sign_y3 *= -1

    if (x2-1180)>20 or x2<20:
        sign_x2 *= -1
        sign_x3 *= -1
    if (y2-880)>20 or y2<20:
        sign_y2 *= -1

    if (x3-1180)>20 or x3<20:
        sign_x3 *= -1
    if (y3-880)>20 or y3<20:
        sign_y3 *= -1
        
    time += 1/FPS

    if time>2:
        color1 = COLORS[randint(0, 5)]
        color2 = COLORS[randint(0, 5)]
        r1 = randint(30,50)
        r2 = randint(30,50)
        time = 0
    
    pygame.display.update()
    screen.fill(BLACK)

print(points,' out of ',count)
pygame.quit()


