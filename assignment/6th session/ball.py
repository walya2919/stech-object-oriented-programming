import random
import pygame

from pygame.locals import *

class Ball():

    def __init__(self, window, window_width, window_height):
        self.window = window  # remember the window, so we can draw later
        self.window_width = window_width
        self.window_height = window_height

        self.image = pygame.image.load('images/ball.png')
        # A rect is made up of [x, y, width, height]
        ball_rect = self.image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.max_width = window_width - self.width
        self.max_height = window_height - self.height
        
        # Pick a random starting position 
        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speeds = [-4, -3, -2, -1, 1, 2, 3, 4] 
        self.x_speed = random.choice(speeds)
        self.y_speed = random.choice(speeds)

    def update(self):
        # Check for hitting a wall.  If so, change that direction.
        if (self.x < 0) or (self.x >= self.max_width):
            self.x_speed = -self.x_speed

        if (self.y < 0) or (self.y >= self.max_height):
            self.y_speed = -self.y_speed

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        self.rect.update(self.x, self.y, self.width, self.height)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
