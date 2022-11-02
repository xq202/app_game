from mimetypes import init
from turtle import width
import pygame
from pygame.locals import *
import button_app
import setting
import open_file
import os
pygame.init()
dis = pygame.display.set_mode((setting.width,setting.height))
bt = button_app.butoon(50,50)
clock  = pygame.time.Clock()
while setting.app_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.app_running = False
    dis.fill('white')
    a = pygame.mouse.get_rel()
    if bt.draw(dis,setting.x,setting.y):
        open_file.openFiles()
        os.system(setting.dirfile)
    bt.draw(dis,setting.x,setting.y)
    clock.tick(setting.fps)
    pygame.display.update()