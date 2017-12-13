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

# score = 000
# balls = 0

#def add_Score(digit, rank):
#    if rank == rHundreds:
#        if digit != 9:
#    return str("digit")

# draw the black background onto the surface
windowSurface.fill(BLACK)

# draw stuffs to screen
digitalFont = pygame.font.Font("digital.ttf", 350) # font argument needs full path if not in this folder

# hundreds = digitalFont.render(str("9"), 1, GREEN)
# tens = digitalFont.render("9", 1, GREEN)
ones = digitalFont.render("999", 1, GREEN)
balls = digitalFont.render("9", 1, RED)

width = ones.get_width()
height = ones.get_height()
centeredTopBottom = windowSurface.get_height() // 2 - height // 2

# (x,y)
windowSurface.blit(ones, (20, centeredTopBottom))
# windowSurface.blit(hundreds, (20, windowHeight))
# windowSurface.blit(tens, (20 + width + 10, windowHeight))
# windowSurface.blit(ones, (20 + 2 * width + 10 + 10, windowHeight))
windowSurface.blit(balls, (20 + 3 * (width // 3) + 10 + 10 + 40, centeredTopBottom))

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
