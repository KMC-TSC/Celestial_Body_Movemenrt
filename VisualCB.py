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
G = 6.674 * pow(10,-11)
Bodies=[]

class Planet:
    def __init__(self, Name:str, Mass:float, Radius:float, Xposition:float, Yposition:float, VeloX:float, VeloY:float, Scale:float):       
        self.Name = Name
        self.Mass = Mass
        self.Radius = Radius 
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.VeloX = VeloX
        self.VeloY = VeloY
        self.Scale = Scale
        self.update_text()
        Bodies.append(self)
        

    def ChangeRadius(self, NewRadius:float):
        self.Radius= NewRadius
    def ChangeMass(self, NewMass:float):
        self.Mass= NewMass
    def ChangeName(self, NewName:str):
        self.Name= NewName  

    def Rotate(self, angle_degrees:float):
        angle = math.radians(angle_degrees)
        x, y = self.Xposition, self.Yposition
        self.Xposition = (x*math.cos(angle) - y*math.sin(angle))
        self.Yposition = (x*math.sin(angle) + y*math.cos(angle))

    def AccDueTo(self,other:Planet):
        Radius = math.sqrt (((self.Xposition-other.Xposition)+(self.Yposition-other.Yposition))) 
        return (G*other.Mass)/pow(Radius,2)
    
    #def Accelerate(self, AccDueTo(other)):
        
        
    def Create(self,Colour):
        if (self.VeloX < 0) or (self.VeloX >0):
            self.Xposition += self.VeloX
        if (self.VeloY < 0) or (self.VeloY >0):
            self.Yposition += self.VeloY
        self.Colour = Colour
        pg.draw.circle(window,(self.Colour),(self.Xposition,self.Yposition),self.Radius/self.Scale)
        window.blit(self.text, (self.Xposition-((self.Radius/self.Scale)/2), self.Yposition-(self.Radius/self.Scale)-30))

    def update_text(self):
        font_size = max(15, int((self.Radius/self.Scale) * 0.9))  # Prevent font size from being too small
        TextFont = pg.font.Font(None, font_size)
        self.text = TextFont.render(self.Name, True, 'White')

    
        
print("--[TEST AREA]--")  
d = Planet("Sun", 120000, 695950, 100, 200,0.5,0.7,19000)
print(f"Radius of {d.Name} is {d.Radius}")
print(f"Mass of {d.Name} is {d.Mass}")
print(f"Original Coordinates of {d.Name} are ({d.Xposition},{d.Yposition})")
print(Bodies)

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