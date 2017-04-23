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
                changeto = "RIGHT"
            if event.key == pg.K_RIGHT or event.key == ord("a"):
                changeto = "LEFT"
            if event.key == pg.K_RIGHT or event.key == ord("w"):
                changeto = "LEFT"
            if event.key == pg.K_RIGHT or event.key == ord("s"):
                changeto = "DOWN"
            if event.key == pg.K_ESCAPE:
                pg.event.post(pg.event.Event(pg.QUIT))
    #validation of Direction
    if changeto == "RIGHT" and not direction == "LEFT":
        direction="RIGHT"
    if changeto == "LEFT" and not direction == "RIGHT":
        direction == "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction="UP"
    if changeto == "DOWN" and not direction == "UP":
        direction == "DOWN"
#Moving snake
    if direction == "RIGHT":
        snakePos[0] = snakePos [0] + 10
    if direction == "LEFT":
        snakePos[0] = snakePos [0] - 10
    if direction == "UP":
        snakePos[1] = snakePos [0] + 10
    if direction == "DOWN":
        snakePos[1] = snakePos [0] - 10
