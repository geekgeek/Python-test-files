#https://www.youtube.com/watch?v=EHOYMe2HS8M
#http://pygame.org/docs/ref/event.html

import pygame
pygame.init()

#Variables
colorWhite = (255,255,255)
colorBlack = (0,0,0)
colorRed = (255,0,0)
colorGreen =(0,255,0)
colorBrown =(153,76,0)
colorYellow = (255,255,0)
#</>


gameDisplay = pygame.display.set_mode((800,600))

#title
pygame.display.set_caption('Slither')
#</>


gameExit = False

lead_x = 300
lead_y = 300

lead_x_change = 0
lead_y_change = 0

#define clock
clock = pygame.time.Clock()

#http://pygame.org/docs/ref/event.html
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
                
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

    if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y < 0: #boundaries
        gameExit = True


    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(colorWhite)
    pygame.draw.rect(gameDisplay, colorBlack, [lead_x,lead_y,10,10]) # draw rectangle
    
    pygame.display.update() #update display

    clock.tick(30) #frames per second
            
        
#unitialising pygame
pygame.quit()
#</>

#exit python
quit() 
#</>












#CUSTOM FUNCTIONS
#game_loop show events
def showmyEventts():
    while not gameExit:
        for event in pygame.event.get():
            print(event)
#</>

def drawSomeThing():
        #Location
    pygame.draw.rect(gameDisplay, colorBlack, [10,50,780,10]) # draw rectangle
    
    pygame.draw.rect(gameDisplay, colorGreen, [0,550,800,10]) # draw rectangle
    pygame.draw.rect(gameDisplay, colorBlack, [0,560,800,40]) # draw rectangle

    #Character
    pygame.draw.rect(gameDisplay, colorBrown, [100,400,40,40]) # draw rectangle
    pygame.draw.rect(gameDisplay, colorBlack, [100,380,60,20]) # draw rectangle
    pygame.draw.rect(gameDisplay, colorBlack, [100,440,60,20]) # draw rectangle

    #Enemies
    pygame.draw.rect(gameDisplay, colorYellow, [550,440,60,20]) # draw rectangle
    pygame.draw.rect(gameDisplay, colorYellow, [450,300,60,20]) # draw rectangle
    pygame.draw.rect(gameDisplay, colorYellow, [500,200,60,20]) # draw rectangle
