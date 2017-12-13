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

# draw the black background onto the surface
windowSurface.fill(BLACK)

# draw stuffs to screen
digitalFont = pygame.font.Font("digital.ttf", 350) # font argument needs full path if not in this folder

score = digitalFont.render("999", 1, GREEN)
balls = digitalFont.render("9", 1, RED)

width = score.get_width()
height = score.get_height()
centeredTopBottom = windowSurface.get_height() // 2 - height // 2

# (x,y)
windowSurface.blit(score, (20, centeredTopBottom))
# windowSurface.blit(balls, (20 + 3 * (width // 3) + 10 + 10 + 40, centeredTopBottom))
windowSurface.blit(balls, (windowSurface.get_width() - balls.get_width() - 20, centeredTopBottom))

# draw the window onto the screen
pygame.display.update()

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
                pygame.quit()
                sys.exit()
            # if event.key == pygame.K_RIGHT:
            #
            # if event.key == pygame.K_UP:
            #
            # if event.key == pygame.K_DOWN:
