import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
pygame.font.init()

# set up the window
windowSurface = pygame.display.set_mode((800, 480), 0, 32)
pygame.display.set_caption('Skee Ball')

# set up the colors (red, green, blue)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

SCORE = 000
BALLS = 0

def updateGame(keyScore):
    global BALLS, SCORE
    if (BALLS < 9):
        BALLS += 1
        SCORE += keyScore
    elif (BALLS == 9):
        BALLS = 0
        SCORE = 000

# run the game loop
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

            # if event.key == pygame.K_RIGHT:
            #
            # if event.key == pygame.K_UP:
            #
            # if event.key == pygame.K_DOWN:

    # definitions
    digitalFont = pygame.font.Font("digital.ttf", 350) # font argument needs full path if not in this folder
    score = digitalFont.render(str(SCORE), 1, GREEN)
    balls = digitalFont.render(str(BALLS), 1, RED)
    centeredTopBottom = windowSurface.get_height() // 2 - score.get_height() // 2

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # (x,y)
    windowSurface.blit(score, (20, centeredTopBottom))
    windowSurface.blit(balls, (windowSurface.get_width() - balls.get_width() - 20, centeredTopBottom))

    # draw the window onto the screen
    pygame.display.update()
