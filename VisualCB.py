import numpy as np
import pygame as pg
from sys import exit
import math

pg.init()
window = pg.display.set_mode((1000,500))
Clock = pg.time.Clock()
pg.display.set_caption('CELESTIAL BODIES DEMO')  
SpaceImage1 = pg.image.load('Space2.jpeg').convert_alpha()
SpaceImage1 = pg.transform.scale(SpaceImage1, (500, 500))

class Planet:
    def __init__(self, Name, Mass, Radius, Xposition, Yposition,VeloX,VeloY):       
        self.Name = Name
        self.Mass = Mass
        self.Radius = Radius
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.VeloX = VeloX
        self.VeloY = VeloY
        self.update_text()
        

    def update_text(self):
        font_size = max(15, int(self.Radius * 0.9))  # Prevent font size from being too small
        TextFont = pg.font.Font(None, font_size)
        self.text = TextFont.render(self.Name, True, 'White')

    def ChangeRadius(self, NewRadius):
        self.Radius= NewRadius
    def ChangeMass(self, NewMass):
        self.Mass= NewMass
    def ChangeName(self, NewName):
        self.Name= NewName  

    def Rotate(self, angle_degrees):
        angle = math.radians(angle_degrees)
        x, y = self.Xposition, self.Yposition
        self.Xposition = (x*math.cos(angle) - y*math.sin(angle))
        self.Yposition = (x*math.sin(angle) + y*math.cos(angle))


    def Create(self,Colour):
        if (self.VeloX < 0) or (self.VeloX >0):
            self.Xposition += self.VeloX
        self.Colour = Colour
        pg.draw.circle(window,(self.Colour),(self.Xposition,self.Yposition),self.Radius)
        window.blit(self.text, (self.Xposition-(self.Radius/2), self.Yposition-self.Radius-30))
        
print("--[TEST AREA]--")  
d = Planet("Sun", 120000, 10, 100, 200,3,0)
print(f"Radius of {d.Name} is {d.Radius}")
print(f"Mass of {d.Name} is {d.Mass}")
print(f"Original Coordinates of {d.Name} are ({d.Xposition},{d.Yposition})")

print("--[TEST AREA]--")    

while True:
    window.blit(SpaceImage1,(0,0))
    d.Create((225,225,0))  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    Clock.tick(30)