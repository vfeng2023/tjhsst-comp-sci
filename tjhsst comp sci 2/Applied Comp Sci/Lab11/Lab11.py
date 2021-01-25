#Name: Karthik and Vivan
#Date: 10/23/2019

import webbrowser
from PIL import Image
from turtle import Turtle
from random import randint

img = Image.new('RGB',(640, 480),(255,254,253))

turtlePixels = 0


j = open('Lab11.txt','w')
for i in range(1,801):
   turt = Turtle(img, 320, 450,90, (0,0,0))
   n = 128
   npixels = 0 #New Pixels
   for k in range(9):
      ip = turt.move(n) #Iteration Pixels
      r = randint(1,2)
      if r == 1:
         turt.turn(30)
      elif r==2:
         turt.turn(-30)
      n = n*0.75
      turtlePixels += ip
      npixels += ip
   j.write(str(i) + " "+str(turtlePixels)+ " "+ str(npixels)+'\n')
  

         
j.close()   




img.save('random_tree.png')
webbrowser.open('random_tree.png')