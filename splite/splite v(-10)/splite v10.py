
import pygame,sys,pygame.mixer
import random
from pygame.locals import *


pygame.init()
scale_x=1370
scale_y=700
scale_r=50
gameDisplay = pygame.display.set_mode((scale_x,scale_y),HWSURFACE|DOUBLEBUF|RESIZABLE)
bg = pygame.image.load("bg.png")
gameDisplay.blit(pygame.transform.scale(bg,(scale_x,scale_y)),(0,0))
pygame.display.set_caption('splite')
pygame.display.flip()
gameExit=False
white=(255,255,255)
red=(150,150,150)
x=scale_x/2
y=scale_y/2
keydown=True
xc=0
yc=0
xn=0
yn=0
enemies=True
clock= pygame.time.Clock()
spaceship=pygame.image.load("spaceship.png")
spaceship.set_colorkey((255,255,255))
enemy=pygame.image.load("sp1.png")
enemy.set_colorkey((0,0,0))
kdown=False
mr=0
ml=0
mu=0
md=0
fl=scale_y/200
x_bullet=[]
y_bullet=[]
game_pause=False
user_blockx=50
enemy_blockx=50
user_blocky=100
enemy_blocky=50
kdownl=False
kdownr=False
kdownu=False
Kdownd=False
tele=500
xn=1
yn=0


while True:
    pygame.event.pump()
    event=pygame.event.wait()
    if event.type==QUIT: pygame.display.quit()
    elif event.type==VIDEORESIZE:
        gameDisplay=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
        gameDisplay.blit(pygame.transform.scale(bg,event.dict['size']),(0,0))
        pygame.display.flip()
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit = True
    
            if event.type == pygame.KEYDOWN:
                kdown=True
                if event.key == pygame.K_LEFT:
                    ml = - fl
                    kdownl=True
                if event.key == pygame.K_RIGHT:
                    mr = + fl
                    kdownr=True
                if event.key == pygame.K_UP:
                    mu = - fl
                    kdownu=True
                if event.key == pygame.K_DOWN:
                    md = + fl
                    kdownd=True
                if event.key == pygame.K_m:
                    if kdownl==True:
                        x=x-tele
                    if kdownr==True:
                        x=x+tele
                    if kdownu==True:
                        y=y-tele
                    if kdownd==True:
                        y=y+tele
                    
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ml=0
                    kdownl=False
                if event.key == pygame.K_RIGHT:
                    mr=0
                    kdownr=False
                if event.key == pygame.K_UP:
                    mu=0
                    kdownu=False
                if event.key == pygame.K_DOWN:
                    md=0
                    kdownd=False
        
        if x < 5:
            x=5
        if y < 5:
            y=5
        if y > scale_y-100:
            y=scale_y-100
        if x > scale_x-100:
            x = scale_x-100
        x = x+ml+mr
        y = y+mu+md
        xn =xn+10
        yn =yn+10
        
        if xn > scale_x:
            xn=0
        if yn > scale_y:
            yn=0
        if xn < 0:
            xn=scale_x
        if yn <0:
            yn=scale_y
        
        if x >= (xn-user_blockx) and  x <= (xn+enemy_blockx) and y >= (yn-user_blocky) and y <= (yn+enemy_blocky) :
            print ("game over")
            game_pause=True
        
        if game_pause==True:
            gameExit=True
        
        gameDisplay.fill(white)
        gameDisplay.blit(spaceship, (x, y))
        gameDisplay.blit(enemy, (xn,yn))
    
        pygame.display.flip()
        clock.tick(((scale_x+scale_y)/2)/16)
    pygame.quit()
    quit