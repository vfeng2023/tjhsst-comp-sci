#Name: Vivian and ...

#Date: 10/18/2019

from PIL import Image
import webbrowser
from math import ceil
n = 600
img = Image.new('RGB',(n,n),(255,254,253))
x = 0
y = 1
pt1 = [0.05,0.05]
pt2 = [0.95,0.05]
pt3 = [0.95,0.95]
pt4 = [0.05,0.95]


points = [pt1,pt2,pt3,pt4]

def drawLine(ptX1,ptX2, ptY1, ptY2):
  t = 0.0
  while t < 1.0:
    x = int(n * (ptX1 + t * (ptX2 - ptX1)))
    y = int(n * (ptY1 + t * (ptY2 - ptY1)))
    img.putpixel((x,y),(56,34,63))
    t += 0.001
    
  
    
      
def movey(y1,y2):
   ydist = float(y2 - y1)
   ty = 0.1
   y1 += ty * ydist
   return y1

def movex(x1,x2):
   xdist = x2 - x1
   tx = 0.1
   x1 += tx * xdist
   return x1
   
def drawSquare():
   drawLine(pt1[x],pt1[y],pt2[x],pt2[y])
   drawLine(pt2[x],pt2[y],pt3[x],pt3[y])
   drawLine(pt3[x],pt3[y],pt4[x],pt4[y])
   

def spiral():
   sc = 0
   x = 0
   y = 1
   pt1 = [0.05,0.05]
   pt2 = [0.95,0.05]
   pt3 = [0.95,0.95]
   pt4 = [0.05,0.95]
   drawLine(pt1[x],pt1[y], pt2[x], pt2[y])
   drawLine(pt2[x],pt2[y], pt3[x], pt3[y])
   drawLine(pt3[x],pt3[y], pt4[x], pt4[y])
   drawLine(pt4[x],pt4[y], pt1[x], pt1[y])
   while sc < 50:
      for point in points:
         if points.index(point) == 3:
            next = points[0]      
         else:
            next = points[points.index(point)+1]
         
         point[x] = movex(point[x],next[x])
         point[y] = movey(point[y], next[y])
         drawLine(points[points.index(point)][x],points[points.index(point)][y],points[points.index(next)][x],points[points.index(next)][y])   
      
     
      sc+=1
    

       
spiral()

img.save('lab09.png')
webbrowser.open('lab09.png')
