import pygame

from pygame.locals import *

class SimpleText():
    
    def __init__(self, window, loc, value, text_color):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = text_color
        self.text = None # so that the call to setText below will force the creation of the text image
        self.set_text(value) # set the initial text for drawing

    def set_text(self, new_text):  
        if self.text == new_text:
            return  # nothing to change

        self.text = new_text  # save the new text
        self.textSurface = self.font.render(self.text, True, self.text_color)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)
