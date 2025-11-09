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
Distance_Scale=332500

class Planet:
    def __init__(self, Name:str, Mass:float, Radius:float, Xposition:float, Yposition:float, VeloX:float, VeloY:float, Scale:float):       
        self.Name = Name
        self.Mass = Mass*pow(10,24)
        self.Radius = Radius 
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.VeloX = VeloX
        self.VeloY = VeloY
        self.Scale = Scale
        self.update_text()
        

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

    def XAccDueTo(self,other:Planet):
        Radius = math.sqrt ((pow((self.Xposition-other.Xposition),2)+pow((self.Yposition-other.Yposition),2))) 
        if (self.Yposition-other.Yposition) == 0:
            angle = math.pi/2 if (self.Xposition-other.Xposition) > 0 else -math.pi/2
        else:
            angle = math.atan((self.Xposition-other.Xposition)/(self.Yposition-other.Yposition))
        Acc = (G*other.Mass)/pow(Radius*Distance_Scale,2)
        XAcc = (math.cos(angle)*Acc)/Distance_Scale
        self.VeloX+=XAcc
         
    def YAccDueTo(self,other:Planet):
        Radius = math.sqrt ((pow((self.Xposition-other.Xposition),2)+pow((self.Yposition-other.Yposition),2))) 
        if (self.Yposition-other.Yposition) == 0:
            angle = math.pi/2 if (self.Xposition-other.Xposition) > 0 else -math.pi/2
        else:
            angle = math.atan((self.Xposition-other.Xposition)/(self.Yposition-other.Yposition))
        Acc = (G*other.Mass)/pow(Radius*Distance_Scale,2)
        YAcc = (math.sin(angle)*Acc)/Distance_Scale
        self.VeloY+=YAcc
         
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
d = Planet("Sun", 1989100, 695950, 250, 250,0.0,0.0,19000)
print(f"Radius of {d.Name} is {d.Radius}")
print(f"Mass of {d.Name} is {d.Mass}")
print(f"Original Coordinates of {d.Name} are ({d.Xposition},{d.Yposition})")
e = Planet("Earth", 5.97, 6371, 50, 250,0.0,0.0,350)
print(f"Radius of {d.Name} is {d.Radius}")
print(f"Mass of {d.Name} is {d.Mass}")
print(f"Original Coordinates of {d.Name} are ({d.Xposition},{d.Yposition})")

print("--[TEST AREA]--")    

while True:
    window.blit(SpaceImage1,(0,0))
    d.Create((225,225,0))  
    e.Create((73,157,208))
    e.XAccDueTo(d)
    e.YAccDueTo(d)
    d.XAccDueTo(e)
    d.YAccDueTo(e)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    Clock.tick(30)