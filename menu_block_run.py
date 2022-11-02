from tkinter import font
import pygame 
from pygame.locals import *
class game_event:
    def __init__(self, string, size, width,height,x,y):
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.surface = pygame.Surface((self.width,self.height),SRCALPHA)
        pygame.draw.line(self.surface,"brown",(0,0),(0,self.height),20)
        pygame.draw.line(self.surface,"brown",(0,0),(self.width,0),20)
        pygame.draw.line(self.surface,"brown",(self.width,0),(self.width,self.height),20)
        pygame.draw.line(self.surface,"brown",(0,self.height),(self.width,self.height),20)
        self.font = pygame.font.Font(None,size)
        self.surface.fill((255,255,200))
        text = self.font.render(string,True,"black")
        self.surface.blit(text,(self.width/6+10,self.height/6))
    def draw(self,dis):
        dis.blit(self.surface,(self.x,self.y))