#https://www.youtube.com/watch?v=PzG-fnci8uE

import pygame
import time
pygame.init()

#Variables
colorWhite = (255,255,255)
colorBlack = (0,0,0)
colorRed = (255,0,0)
colorGreen =(0,255,0)
colorBrown =(153,76,0)
colorYellow = (255,255,0)

display_width = 800
display_height = 600
#</>


gameDisplay = pygame.display.set_mode((display_width,display_height))

#title
pygame.display.set_caption('Slither')
#</>


gameExit = False

lead_x = display_width/2
lead_y = display_height/2

lead_x_change = 0
lead_y_change = 0

#define clock
clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


#http://pygame.org/docs/ref/event.html
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
                
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0: #boundaries
        gameExit = True


    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(colorWhite)
    pygame.draw.rect(gameDisplay, colorBlack, [lead_x,lead_y,block_size,block_size]) # draw rectangle
    
    pygame.display.update() #update display

    clock.tick(FPS) #frames per second
            

message_to_screen("You loose", colorRed)
pygame.display.update() #update display

time.sleep(2)
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
