import pygame
from pygame.locals import *
#button class
class Button():
    def __init__(self, text, size_text, color_text, color, width, height, x, y):
        self.surface = pygame.Surface((width,height),SRCALPHA)
        font = pygame.font.Font(None,size_text)
        mess = font.render(text,True,color_text)
        self.surface.fill(color)
        self.surface.blit(mess,(13,8))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.surface, (self.rect.x, self.rect.y))

        return action