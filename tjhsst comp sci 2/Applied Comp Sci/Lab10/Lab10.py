#Name: Vivian Feng
#Date: 10/21/2019

import webbrowser
from PIL import Image
from turtle import Turtle

img = Image.new('RGB',(600,600),(255,254,253))

t1 = Turtle(img,150,150,0,(0,0,0))
t2 = Turtle(img,450,150,0,(0,0,0))
t3 = Turtle(img,300,450,0,(0,0,0))

#this function draws a polygon
def draw_polygon(turt,length,sides):
   turn_amt = 360.0/sides
   total_deg = 0
   while total_deg < 360:
      turt.move(length)
      turt.turn(turn_amt)
      total_deg += turn_amt

#this function draws a spinning polygon      
def spinning_polygon(turt,length,sides,increment):
   total_spin = 0
   while total_spin < 360:
      draw_polygon(turt,length,sides)
      turt.turn(increment)
      total_spin += increment
      
#this function draws a spiral

def draw_spiral(turt,increment2,move_amt):
   for leg in range(20):
      turt.move(move_amt)
      turt.turn(-90)
      move_amt += increment2

#draw pentagon
draw_polygon(t1,75,5)

#draw spinning polygon, turning after each
spinning_polygon(t2,60,6,60)
#draw spiral, starting at (300,300), incrementing each side by XX pixels
draw_spiral(t3,10,10)   

img.save('polygons.png')
webbrowser.open('polygons.png')

