# Notes ------------------------------------------------------------------------
# - continues to accumulate points during game finish animations
# - needs two player capability
# - GPIO library added and basic code to take input sensors
# -
# -
#-------------------------------------------------------------------------------

# import libraries -------------------------------------------------------------
import pygame, sys
from pygame.locals import *
#-------------------------------------------------------------------------------

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
def wait(int = 0):
    if (int == 1):
        pygame.time.delay(500)
    else:
        pygame.time.delay(200)

def updateGame(keyScore):
    global BALLS, SCORE

    if (BALLS < 9):
        BALLS += 1
        SCORE += keyScore
        # pygame.display.update()
    elif (BALLS == 9):
        for x in range(3):
            wait(1)
            windowSurface.fill(BLACK)
            pygame.display.update()

            wait(1)
            windowSurface.blit(score, (20, centeredTopBottom))
            windowSurface.blit(balls, (windowSurface.get_width() \
                                - balls.get_width() - 20, centeredTopBottom))
            pygame.display.update()

        for i in range(3):
            numberAnimation = ["aaa", "bbb", "ccc", "ddd", "eee", "fff"]
            digitalFont = pygame.font.Font("digital.ttf", 350)

            for object in numberAnimation:
                wait()
                windowSurface.fill(BLACK)
                scene = digitalFont.render(object, 1, GREEN)
                windowSurface.blit(scene, (20, centeredTopBottom))
                windowSurface.blit(balls, (windowSurface.get_width() \
                                - balls.get_width() - 20, centeredTopBottom))
                pygame.display.update()

        wait()
        BALLS = 0
        SCORE = 000
        pygame.display.update()
#-------------------------------------------------------------------------------

# game loop --------------------------------------------------------------------
while True:
    global BALLS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:

            if (BALLS )
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
    # new = digitalFont.render("aaa", 1, GREEN)
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
