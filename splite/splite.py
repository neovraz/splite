import pygame
import random

def home_scrdraw1():
    cont=pygame.image.load("Continue.bmp")
    home_Display.blit(pygame.transform.scale(cont,(325,100)),(233,300))
def home_scrdraw2():
    cont_sel=pygame.image.load("Continue_sel.bmp")
    home_Display.blit(pygame.transform.scale(cont_sel,(325,100)),(233,300))
def home_scrdraw3():
    home_Display.blit(pygame.transform.scale(cont_sel,(325,100)),(233,300))
    new=pygame.image.load("newgame.bmp")
def home_scrdraw4():
    home_Display.blit(pygame.transform.scale(new,(325,100)),(233,100))
    new_sel=pygame.image.load("newgame_sel.bmp")
def homescr_draw():
    home_Display.blit(pygame.transform.scale(new_sel,(325,100)),(233,100))
    qui_t=pygame.image.load("quit.bmp")
def home_scrdraw():
    home_Display.blit(pygame.transform.scale(qui_t,(154,100)),(233,500))
    quit_sel=pygame.image.load("quit_sel.bmp")

    
def home_scrdraw():
    pygame.init()
    scale_hx=800
    scale_hy=800
    black=(255,255,255)
    home_Display = pygame.display.set_mode((scale_hx,scale_hy))
    home_Display.fill(black)
    cont=pygame.image.load("Continue.bmp")
    home_Display.blit(pygame.transform.scale(cont,(325,100)),(233,300))
    cont_sel=pygame.image.load("Continue_sel.bmp")
    home_Display.blit(pygame.transform.scale(cont_sel,(325,100)),(233,300))
    new=pygame.image.load("newgame.bmp")
    home_Display.blit(pygame.transform.scale(new,(325,100)),(233,100))
    new_sel=pygame.image.load("newgame_sel.bmp")
    home_Display.blit(pygame.transform.scale(new_sel,(325,100)),(233,100))
    qui_t=pygame.image.load("quit.bmp")
    home_Display.blit(pygame.transform.scale(qui_t,(154,100)),(233,500))
    quit_sel=pygame.image.load("quit_sel.bmp")
    home_Display.blit(pygame.transform.scale(qui_t,(154,100)),(233,500))
    pygame.display.flip()
def home_scr():
    
    home_screen=True
    while home_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home_screen = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    home_screen = False
                    
                if event.key==pygame.K_r:
                    game()
                    home_screen=False
    pygame.display.quit()     
        
def game():

    
    pygame.init()
    #pygame.font.init()
    #time_font= pygame.font.SysFont('Comic Sans MS', 30)







    #Display and blit settings ----------------



    scale_x=1370                                #Screen x axis pixels
    scale_y=800                                 #Screen y axis pixels                
    scale_r=50
    gameDisplay = pygame.display.set_mode((scale_x,scale_y))
    bg = pygame.image.load("background.png")
    gameDisplay.blit(pygame.transform.scale(bg,(scale_x,scale_y)),(0,0))
    pygame.display.set_caption('splite')
    pygame.display.flip()


    #colors ---------
    blue=(150,0,255)
    white=(255,255,255)
    red=(255,0,0)

    #Game loop variables ----------------

    game_pause=False                                #Variable for pausing the game



    #Boolean variables ----------------

    end=False
    restart=True
    gameExit=False
    keydown=True
    fire=False                                 #Fire state
    gameover=False

    #Enemy related ----------

    xn=0
    yn=0
    enemy=pygame.image.load("sp1.png")
    enemy1=pygame.image.load("sp1.png")
    enemy.set_colorkey((0,0,0))
    enemy1.set_colorkey((0,0,0))
    xn=1
    yn=0
    xn1=600
    yn1=30
    enemy_dist=1
    enemy_dist1=2                              #Enemy distance covered in one frame



    #clock variables ----------

    clock= pygame.time.Clock()
    time_var=0
    time_var1=0
    TT=70
    orTT=70
    slTT=20
    #Spaceship variables -----------


    x=scale_x/2
    y=scale_y/2
    mr=0
    ml=0
    mu=0
    md=0
    fl=10                                  #Movement per frame
    tele=250                                    #Teleportation distance
    spaceship=pygame.image.load("spaceship.png")
    spaceship.set_colorkey((255,255,255))


    #Score ----------------
    score=5
    kdown=False

    #Gameover variables -----------------


    user_blockx=50                                  #Range of user x axis to be game over
    enemy_blockx=50                                 #Range of enemy x axis to be game over
    user_blocky=100                                 #Range of user x axis 
    enemy_blocky=50                                 #Range of enemy y axis to be game over

    #Keys pressed check ------------


    kdownl=False                                  # Keys present boolean states.
    kdownr=False                                 #kdownr = key down right
    kdownu=False                                #
    kdownd=False                               #






    #Laser related ----------

    xlaser=x+40
    ylaser=-50
    laser_y_width=scale_y-(scale_y-(y+15))
    laser_x_width=15

    #Bait related --------------

    bait=pygame.image.load("bait.jpg")
    bait_dist=5
    randbaitx = random.randrange(50,scale_x-50)
    randbaity = 50

    print("Lets Start")
    x=scale_x/2
    y=scale_y/2
    xn=10
    xn1=scale_x-10
    yn=50
    yn1=scale_y-50
    
    #pygame.event.pump()
    #event=pygame.event.wait()
    #if event.type==QUIT: pygame.display.quit()
    #if event.type==VIDEORESIZE:
        #gameDisplay=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
        #gameDisplay.blit(pygame.transform.scale(bg,event.dict['size']),(0,0))
        #pygame.display.flip()
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit = True
                home_scr()
    
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

                if event.key == pygame.K_SPACE:
                    fire=not fire
                if event.key == pygame.K_n:
                    orTT=TT
                    TT=slTT
            
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
                #if event.key == pygame.K_SPACE:
                 #   fire = False
                if event.key == pygame.K_n:
                    slTT=TT
                    TT=orTT
                if event.key == pygame.K_q:
                    game_pause=True
        if x < 5:
            x=5
        if y < 5:
            y=5
        if y > scale_y-100:
            y=scale_y-100
        if x > scale_x-100:
            x = scale_x-100
        x = x+(ml)+(mr)
        y = y+(mu)+(md)
        yn =yn+enemy_dist1
        yn1 =yn1+enemy_dist1
        
        if xn > scale_x: 
            xn=0
        if yn > scale_y:
            yn=0
            xn=random.randrange(50,scale_x-50)
        if xn < 0:
            xn=scale_x
        if yn <0:
            xn=random.randrange(50,scale_x-50)
            yn=scale_y
        if xn1 > scale_x:
            xn1=0
        if yn1 > scale_y:
            yn1=0
            xn1=random.randrange(50,scale_x-50)
        if xn1 < 0:
            xn1=scale_x
        if yn1 <0:
            yn1=scale_y
            xn1=random.randrange(50,scale_x-50)
        
        if x >= (xn-user_blockx) and  x <= (xn+enemy_blockx) and y >= (yn-user_blocky) and y <= (yn+enemy_blocky) :
            print ("game over")
            game_pause=True
            gameExit=True

        if x >= (xn1-user_blockx) and  x <= (xn1+enemy_blockx) and y >= (yn1-user_blocky) and y <= (yn1+enemy_blocky) :
            print ("game over")
            game_pause=True
            gameExit=True

        if game_pause==True:
            pygame.init()
            while not end:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            pygame.display.quit()
                            pygame.quit()
                            game()
                            game_pause=False
                            end=False
                            
                        if event.key == pygame.K_q:
                            pygame.display.quit()
                            pygame.quit()
                            home_scr()
                            game_pause=False
                            end=False

            
        #gameDisplay.blit(pygame.transform.scale(bg,(scale_x,scale_y)),(0,0))
        gameDisplay.fill(blue)
        
        if fire == True:
            xlaser=x+40
            ylaser=-50
            laser_y_width=scale_y-(scale_y-(y+15))
            laser_x_width=15
            pygame.draw.rect(gameDisplay,red,[xlaser,ylaser,laser_x_width,laser_y_width])
            if randbaitx >= xlaser and randbaitx < 50+xlaser and randbaity <= ylaser+laser_y_width and randbaity > ylaser :
                score=score+3
                
                randbaitx = random.randrange(50,scale_x-50)
                randbaity = 50
                print (score)

            if xn >= xlaser and xn < 50+xlaser and yn <= ylaser+laser_y_width and yn > ylaser :
                score=score+1
                xn = random.randrange(50,scale_x-50)
                yn=0
            if xn1 >= xlaser and xn1 < 50+xlaser and yn1 <= ylaser+laser_y_width and yn1 > ylaser :
                score=score+1
                xn1 = random.randrange(50,scale_x-50)
                yn1=0

                
        if randbaity > scale_y:
            score=score-5
            randbaitx = random.randrange(50,scale_x-50)
            randbaity = 50
            print (score)
                
        randbaity=randbaity+bait_dist
        gameDisplay.blit(spaceship, (x, y))
        gameDisplay.blit(enemy, (xn,yn))
        gameDisplay.blit(enemy, (xn1,yn1))
        gameDisplay.blit(bait, (randbaitx,randbaity))
        pygame.display.flip()
        time_var=time_var+1
        if time_var%20 == 0:

            print (TT)
        clock.tick((TT))
    return 0

        
a=home_scr()
if a==0:
    pygame.quit()
    quit

