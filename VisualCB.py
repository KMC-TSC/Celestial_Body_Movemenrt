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
Distance_Scale=747989.355

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
        self.angle = angle
    def XAccDueTo(self,other:Planet):
        Radius = math.sqrt ((pow((self.Xposition-other.Xposition),2)+pow((self.Yposition-other.Yposition),2))) 
        if (self.Yposition-other.Yposition) == 0:
            angle = math.pi/2 if (self.Xposition-other.Xposition) > 0 else -math.pi/2
        else:
            angle = math.atan2((self.Yposition-other.Yposition),(self.Xposition-other.Xposition))
        Acc = (G*other.Mass)/pow(Radius*Distance_Scale,2)
        XAcc = -((math.cos(angle)*Acc)/Distance_Scale)
        self.VeloX+=XAcc
        self.XAcc = XAcc
        self.angle = angle
         
    def YAccDueTo(self,other:Planet):
        Radius = math.sqrt ((pow((self.Xposition-other.Xposition),2)+pow((self.Yposition-other.Yposition),2))) 
        if (self.Yposition-other.Yposition) == 0:
            angle = math.pi/2 if (self.Xposition-other.Xposition) > 0 else -math.pi/2
        else:
            angle = -(math.atan((self.Yposition-other.Yposition)/(self.Xposition-other.Xposition)))
        Acc = (G*other.Mass)/pow(Radius*Distance_Scale,2)
        YAcc = (math.sin(angle)*Acc)/Distance_Scale
        self.VeloY+=YAcc
        self.YAcc = YAcc
        
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
Su = Planet("Sun", 1989100, 695950, 250, 250,0.0,0.0,19000)
print(f"Radius of {Su.Name} is {Su.Radius}")
print(f"Mass of {Su.Name} is {Su.Mass}")
print(f"Original Coordinates of {Su.Name} are ({Su.Xposition},{Su.Yposition})")
Er = Planet("Earth", 5.97, 6371, 450, 80,-0.01,1.0,360)
print(f"Radius of {Er.Name} is {Er.Radius}")
print(f"Mass of {Er.Name} is {Er.Mass}")
print(f"Original Coordinates of {Er.Name} are ({Er.Xposition},{Er.Yposition})")

print("--[TEST AREA]--")    
print("--[LIVE AREA]--")   
while True:
    window.blit(SpaceImage1,(0,0))
    Su.Create((225,225,0))  
    Er.Create((73,157,208))
    Er.XAccDueTo(Su)
    Er.YAccDueTo(Su)
    Su.XAccDueTo(Er)
    Su.YAccDueTo(Er)
    print(f"{Er.XAcc}p/f^2   |{Er.YAcc}p/f^2")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    Clock.tick(60)
print("--[LIVE AREA]--")   