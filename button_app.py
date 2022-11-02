import pygame
from pygame.locals import *
import open_file
class butoon():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.surface = pygame.surface.Surface((width,height),SRCALPHA)
        self.rect = self.surface.get_rect()
        self.clicked = False
    def draw(self, dis, x, y):
        action = False
        self.rect.topleft = (x,y)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0]==False:
                self.clicked = False
        pygame.draw.polygon(self.surface,'black',((0,0),(0,self.height),(self.width,self.height),(self.width,0)))
        dis.blit(self.surface,(x,y))
        return action
