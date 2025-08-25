import numpy as np
import pygame as pg
from sys import exit
import math

pg.init()
window = pg.display.set_mode((1000,500))
Clock = pg.time.Clock()
pg.display.set_caption('CELESTIAL BODIES DEMO')  
SpaceImage1 = pg.image.load('Space2.jpeg').convert_alpha()
SpaceImage1 = pg.transform.scale(SpaceImage1, (1000, 500))
x = 0.0
y = -125.0
a = 0.0

while True:
    a+=0.08
    if a > 2*math.pi:
        a = 0
    xp = (x*math.cos(a)-y*math.sin(a))+100
    yp = x*math.sin(a)+y*math.cos(a)
    window.blit(SpaceImage1,(0,0))
    pg.draw.circle(window, (225, 100, 0), (xp+500, yp+250), 50)  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    Clock.tick(30)