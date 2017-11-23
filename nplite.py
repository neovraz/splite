import pygame


pygame.init()

white = (255,255,255)
red = (255,0,0)
scale_x=200
scale_y=400
spawn_pt_x=scale_x/2
spawn_pt_y=scale_y/2
ux=spawn_pt_x
uy=spawn_pt_y
gameExit=False
paused=False



screen = pygame.display.set_mode((scale_x,scale_y))
pygame.display.set_caption('nplite')
pygame.display.update()

class Enemy:
    eny=0
    enx=0
    def enemy_move():
        eny=eny+5
        enx=enx
    if eny==uy-50 or eny+50==uy and enx+50==ux or enx==ux+50:
        def enemy_kill():
            print ('kill')
            
en1=Enemy()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


    while not paused:
 
        screen.fill(white)
        pygame.draw.rect(screen,red,[ux,uy,20,20])
        pygame.display.update()








pygame.quit()
quit()

            
