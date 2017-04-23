import pygame as pg
import sys
import random
import time
from colors import *

pg.init()


#play surface

playSurface = pg.display.set_mode((720,460))
pg.display.set_caption("SNAKE GAME!!!!!")
#fps controller
fpsController = pg.time.Clock()
#important variables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = "RIGHT"
changeto = direction

#Game over Function
def gameOver():
    myFont = pg.font.SysFont("monaco", 72)
    gameOverSurface = myFont.render("Game Over", True, RED)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (360,15)
    playSurface.blit(gameOverSurface,gameOverRect)
    pg.display.flip()
    time.sleep(4)
    pg.quit()
    sys.exit()

#main logic

while(True):
    for event in pg.event.get():
        if(event.type == pg.QUIT):
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT or event.key == ord("d"):
                changeto = 'RIGHT'
            elif event.key == pg.K_LEFT or event.key == ord("a"):
                changeto = 'LEFT'
            elif event.key == pg.K_UP or event.key == ord("w"):
                changeto = 'UP'
            elif event.key == pg.K_DOWN or event.key == ord("s"):
                changeto = 'DOWN'
            elif event.key == pg.K_ESCAPE:
                pg.event.post(pg.event.Event(pg.QUIT))
    #validation of Direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction='RIGHT'
    elif changeto == 'LEFT'and not direction == 'RIGHT':
        direction = 'LEFT'
    elif changeto == 'UP' and not direction == 'DOWN':
        direction='UP'
    elif changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    #snake body grow mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos [0] and snakePos [1] == foodPos[1]:
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playSurface.fill(BLUE)
    for pos in snakeBody:
        pg.draw.rect(playSurface,GREEN,pg.Rect(pos[0],pos[1],10,10))

    pg.draw.rect(playSurface,RED,pg.Rect(foodPos[0],foodPos[1],10,10))


    pg.display.flip()
    fpsController.tick(25)