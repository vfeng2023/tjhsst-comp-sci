# Greg Anderson
#7/13/12
# Turtles

from PIL import Image
from math import sin,cos,pi

class Turtle:
   def __init__(self,im, x=0,y=0,deg=0,color=(0,0,0)):
      self.im = im 
      self.x = x 
      self.y = y 
      self.deg = deg
      self.color = color
      
   def turn(self,degs):
      self.deg =self.deg+degs
      
   def move(self,dist):
      newPixels = 0
      i = 0
      while i < dist:
         if self.im.getpixel((int(self.x),int(self.y))) != self.color:
            self.im.putpixel((int(self.x),int(self.y)),self.color)
            newPixels += 1
            
         self.x += cos(self.deg *pi/180)
         self.y -= sin(self.deg * pi/180)
         i+=1
         
      return newPixels
      
   def jump(self,newX,newY):
      self.x = newX
      self.y = newY
      
