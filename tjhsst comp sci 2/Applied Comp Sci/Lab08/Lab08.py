#Name: Karthik and Vivan
#Date: 10/11/2019

from PIL import Image
from random import randint
from random import random
from random import choice

cg = Image.new('RGB',(600,600),(255,254,253))
w=600
h=600
x1 = 0.5
y1=0.1
x2=0.1
y2=0.9
x3=0.9
y3 = 0.9
x4= random(0,1)
y4 = random(0,1)

f = open('lab08.txt','w')
cg.putpixel((int(x1 * n), int(y1 * n)), (0, 0, 0))
cg.putpixel((int(x2 * n), int(y2 * n)), (0, 0, 0))
cg.putpixel((int(x3 * n), int(y3 * n)), (0, 0, 0))

for trial in range(1,30001):
#    xp1 = int(x1*w)
#    yp1 = int(y1*h)
#    xp2 = int(x2*w)
#    yp2 = int(y2*h)
#    xp3 = int(x3*w)
#    yp3 = int(y3*h)
#    xp4 = int(x4*w)
#    yp4 = int(y4*h)
   cg.putpixel((int(x4 * n), int(y4 * n)), (0, 0, 0))
   r = randint(1,3)
   if r == 1:
      x4 = (x4+x1)/2
      y4 = (y4+y1)/2
      
   elif r == 2:
      x4 = (x4+x2)/2
      y4 = (y4+y2)/2
      
   elif r == 3:
      x4 = (x4+x3)/2
      y4 = (y4+y3)/2
      
    
      
     


     
   
   





















