import pygame as pg
import sys
import random
import time
import tkinter
from colors import *

pg.init()

file = "music.wav"
file2 = "mario.wav"
pg.mixer.init()
sound = pg.mixer.Sound(file)
soundDie = pg.mixer.Sound(file2)
#play surface

playSurface = pg.display.set_mode((720,460))
pg.display.set_caption("SNAKE GAME!!!!!")
#fps controller
fpsController = pg.time.Clock()
#important variables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]
score = 0
gameScreen = tkinter.Tk()
gameScreen.geometry('%dx%d+%d+%d' % (200, 50, 250, 250))
gameScreen.resizable(width=False , height=False)
gameScreen.title("Menu")



foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = "RIGHT"
changeto = direction

#Game over Function
def gameOver():
    global snakePos,snakeBody,foodPos,foodSpawn,direction,changeto,score,gameScreen
    myFont = pg.font.SysFont("monaco", 72)
    gameOverSurface = myFont.render("Game Over", True, RED)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (360,15)
    playSurface.blit(gameOverSurface,gameOverRect)
    showScore(0)
    pg.display.flip()
    time.sleep(4)
    snakePos = [100, 50]
    snakeBody = [[100, 50], [90, 50], [80, 50]]
    score = 0
    foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True
    direction = "RIGHT"
    changeto = direction
    gameScreen = tkinter.Tk()
    gameScreen.geometry('%dx%d+%d+%d' % (200, 50, 450, 250))
    gameScreen.resizable(width=False, height=False)
    gameScreen.title("Menu")
    b = tkinter.Button(gameScreen, text="New Game", command=game)
    c = tkinter.Button(gameScreen, text ="Close",command = done)
    b.pack()
    c.pack()
    gameScreen.mainloop()
    pg.quit()
    sys.exit()

#main logic

def done():
    pg.quit()
    sys.exit()
def showScore(ch=1):
    sFont = pg.font.SysFont("monaco", 30)
    Ssurf = sFont.render("Score : "+str(score),True,WHITE)
    sRect = Ssurf.get_rect()
    if ch == 1:
        sRect.midtop = (80,10)
    else:
        sRect.midtop = (360,120)
    playSurface.blit(Ssurf, sRect)

    fpsController.tick(60)

def game():
    global score,changeto,direction,foodPos,foodSpawn,soundDie,sound
    sound.play(100)
    gameScreen.destroy()
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
            score += 1
            foodSpawn = False
        else:
            snakeBody.pop()

        if foodSpawn == False:
            foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        foodSpawn = True

        playSurface.fill(BLACK)
        for pos in snakeBody:
            pg.draw.rect(playSurface,GREEN,pg.Rect(pos[0],pos[1],10,10))

        pg.draw.rect(playSurface,RED,pg.Rect(foodPos[0],foodPos[1],10,10))

        if snakePos[0]>710 or snakePos[0] <0:
            sound.stop()
            soundDie.play()
            gameOver()
        if snakePos[1]>450 or snakePos[1]<0:
            sound.stop()
            soundDie.play()
            gameOver()

        for block in snakeBody[1:]:
            if snakePos[0]==block[0] and snakePos[1] == block[1]:
                sound.stop()
                soundDie.play()
                gameOver()


        showScore()
        pg.display.flip()
        fpsController.tick(23)

game()