#Рефактор картинки от Дмитриевцева Юрия https://github.com/YuraDmitrievtsev/infa_2020_Dmitrievtsev/blob/master/3.py


import pygame
import numpy as np

pygame.init()

FPS = 30

#Размер окна
screen_width = 875
screen_height = 500
sc = pygame.display.set_mode((screen_width, screen_height))

#Задаем цвета
WHITE = (255, 255, 255)
RED=(200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE=(255,165,0)
BLUE=(0,0,255)
BROWN=(165,42,42)

#Белый фон
sc.fill(WHITE)


#Functions drawing parts of a man

#Рисование волос, смещенных на (х,y), кол-во волос, их цвет, масштаб
def draw_hair(x,y, n, hair_color, scale):
    alpha = np.pi/5                # угол между направлением вправо и направлением на первый волосок
    dalpha = (np.pi-2*alpha)/n     # угол между соседними волосками
    r = 25*scale                        # радиус описанного треугольного волоса
    a = 2*np.pi/3                  # треть полного угла для смещения внутри волоса
    for i in range(n+1):
        POL = []
        x0 = (250 + (100 + 10) * np.cos(alpha))*scale #Координаты центра треугольного волоса
        y0 = (250 - (100 + 10) * np.sin(alpha))*scale
        for j in range(3):
            POL.append([x0 + (r*np.cos(a*j + alpha))*scale + x, y0 - (r*np.sin(a*j + alpha))*scale + y])
        pygame.draw.polygon(sc, hair_color, POL)
        alpha+= dalpha

#Глаза, смещенные вправо на х, их цвет, scale
def draw_eyes(x,y, eye_color, scale):
    pygame.draw.circle(sc, eye_color, (np.int(scale*210) + x, np.int(scale*225) + y), np.int(25*scale))
    pygame.draw.circle(sc, eye_color, (np.int(scale*285) + x, np.int(scale*225) + y), np.int(25*scale))
    pygame.draw.circle(sc, BLACK, (np.int(scale*210) + x, np.int(scale*225) + y), np.int(10*scale))#черные зрачки
    pygame.draw.circle(sc, BLACK, (np.int(scale*285) + x, np.int(scale*225) + y), np.int(10*scale))

#Руки, смещенные вправо на х
def draw_hands(x):
    pygame.draw.line(sc, YELLOW, [np.int(scale*150) + x, np.int(scale*400) + y], [np.int(scale*50) + x, np.int(scale*50) + y], np.int(scale*15))
    pygame.draw.line(sc, YELLOW, [np.int(scale*350) + x, np.int(scale*400) + y], [np.int(scale*450) + x, np.int(scale*50) + y], np.int(scale*15))

#Майка, смещенная вправо на х, цвет
def draw_shirt(x,y, shirt_color, scale):
    pygame.draw.circle(sc, shirt_color, (np.int(scale*250) + x, np.int(scale*500) + y), np.int(scale*175))

    #1 Рукав майки
    x0 = np.int(scale*140) + x
    y0 = np.int(scale*365) + y
    r = np.int(scale*45)
    a = 2*np.pi/5
    POL = []
    for i in range(5):
        POL.append([x0 + np.int(scale*(r*np.cos(a*i))),y0 + np.int(scale*(r*np.sin(a*i)))])

    pygame.draw.polygon(sc, shirt_color, POL)

    #2 Рукав майки
    x0 = np.int(scale*360) + x
    y0 = np.int(scale*365) + y
    r = np.int(scale*45)
    a = 2*np.pi/5
    POL = []
    for i in range(5):
        POL.append([np.int(scale*(-r*np.cos(a*i))) + x0, np.int(scale*(-r*np.sin(a*i))) + y0])

    pygame.draw.polygon(sc, shirt_color, POL)

#Голова
def draw_head(x,y,scale):
    pygame.draw.circle(sc, YELLOW, (np.int(scale*250) + x, np.int(scale*250) + y), np.int(scale*100))

#Руки
def draw_hands(x,y,scale):
    pygame.draw.circle(sc, YELLOW, (np.int(scale*50) + x, np.int(scale*50) + y), np.int(scale*25))
    pygame.draw.circle(sc, YELLOW, (np.int(scale*450) + x, np.int(scale*50) + y), np.int(scale*25))
    pygame.draw.line(sc, YELLOW, [np.int(scale*150) + x, np.int(scale*400) + y], [np.int(scale*50) + x, np.int(scale*50) + y], np.int(scale*15))
    pygame.draw.line(sc, YELLOW, [np.int(scale*350) + x, np.int(scale*400) + y], [np.int(scale*450) + x, np.int(scale*50) + y], np.int(scale*15))

#Рот
def draw_mouth(x,y,scale):
    pygame.draw.polygon(sc, RED, [[np.int(scale*250) + x,np.int(scale*325) + y],[np.int(scale*200) + x,np.int(scale*300) + y],[np.int(scale*300) + x,np.int(scale*300) + y]])

#Нос
def draw_nose(x,y,scale):
    pygame.draw.polygon(sc, BROWN, [[np.int(scale*250) + x,np.int(scale*275) + y],[np.int(scale*240) + x,np.int(scale*250) + y],[np.int(scale*260) + x,np.int(scale*250) + y]])

#Функция рисующая мужика, смещенного на (x,y)
def DRAW_PUNK(x,y,scale, hair_color, shirt_color, eye_color):

    draw_hands(x,y,scale)
    draw_shirt(x,y, shirt_color, scale)
    draw_head(x,y, scale)
    draw_mouth(x,y, scale)
    draw_nose(x,y, scale)
    draw_hair(x,y, 10, hair_color,scale)
    draw_eyes(x,y, eye_color,scale)

#Рисование людей
DRAW_PUNK(10 ,-150 ,0.8 , PINK, ORANGE, BLUE)
DRAW_PUNK(400 ,0 ,1.1 , BLUE, RED, GREEN)



#Табличка
pygame.draw.polygon(sc, GREEN, [[15, 50], [15, 0], [screen_width-15, 0], [screen_width-15, 50]])

#Рисование надписи
font = pygame.font.Font(None, 50)
text = font.render("Python is REALLY SUPER DUPER AMAZING!!!", True, BLACK)
textpos = (75, 12)
sc.blit(text, textpos)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
