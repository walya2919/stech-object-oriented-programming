import sys
import pygame

from ball import Ball
from simple_text import SimpleText
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
BALL_WIDTH_HEIGHT = 100
BALL_MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
BALL_MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TEXT_XY = (0, 0)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
text_box = SimpleText(window, (0, 0), '', WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if ball.rect.collidepoint(event.pos):
                text_box.set_text(str(event.pos))
        
    ball.update()

    window.fill(BLACK)

    ball.draw()
    text_box.draw()

    pygame.display.update()

    clock.tick(FPS)

