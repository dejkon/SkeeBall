import pygame, sys
from pygame.locals import *

# set up pygame and window -----------------------------------------------------
pygame.init()
pygame.font.init()
windowSurface = pygame.display.set_mode((800, 480), 0, 32)
pygame.display.set_caption('Skee Ball')
#-------------------------------------------------------------------------------

# variable defs ----------------------------------------------------------------
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

SCORE = 000
BALLS = 0

# function defs
def wait():
    pygame.time.delay(500)

def updateGame(keyScore):
    global BALLS, SCORE

    if (BALLS < 9):
        BALLS += 1
        SCORE += keyScore
        # pygame.display.update()
    elif (BALLS == 9):
        for x in range(3):
            wait()
            windowSurface.fill(BLACK)
            pygame.display.update()
            wait()
            windowSurface.blit(score, (20, centeredTopBottom))
            windowSurface.blit(balls, (windowSurface.get_width() \
                                - balls.get_width() - 20, centeredTopBottom))
            pygame.display.update()

        # pygame.time.delay(500)
        wait()
        BALLS = 0
        SCORE = 000
        # pygame.display.update()
#-------------------------------------------------------------------------------

# game loop ------------------------------------------------------------
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_1:
                updateGame(10)
            if event.key == pygame.K_2:
                updateGame(20)
            if event.key == pygame.K_3:
                updateGame(30)
            if event.key == pygame.K_4:
                updateGame(40)
            if event.key == pygame.K_5:
                updateGame(50)
            if event.key == pygame.K_9:
                updateGame(100)
            if event.key == pygame.K_0:
                updateGame(0)

    # definitions # font argument needs full path if not in this folder
    digitalFont = pygame.font.Font("digital.ttf", 350)
    score = digitalFont.render(str(SCORE).zfill(3), 1, GREEN)
    balls = digitalFont.render(str(BALLS), 1, RED)
    centeredTopBottom = windowSurface.get_height() // 2 \
                        - score.get_height() // 2

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # (x,y)
    windowSurface.blit(score, (20, centeredTopBottom))
    windowSurface.blit(balls, (windowSurface.get_width() \
                        - balls.get_width() - 20, centeredTopBottom))

    # draw the window onto the screen
    pygame.display.update()
#-------------------------------------------------------------------------------
