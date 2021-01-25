#Name: Vivian and Karthik
#Date:9/16/2019

from pyKarel import *
from Athlete import Athlete

maze = raw_input("What maze will you use?(maze1,maze2,maze3) ")

wld = World(maze,width=10,height=10)

karel = Athlete(wld,1,1)

active = True
while active:
   if not karel.frontIsClear():
      clear = 0
      if karel.leftIsClear():
         clear += 1
         
      if karel.rightIsClear():
         clear += 1
         
      if clear == 2:
         karel.turnRight()
         
      elif clear == 1:
         if karel.leftIsClear():
            karel.turnLeft()
         
         if karel.rightIsClear():
            karel.turnRight()
      
      else:
         karel.turnAround()
         
   else:     
      if karel.rightIsClear():
         karel.turnRight()
   
   if not karel.nextToABeeper():        
      karel.move()
   
wld.mainloop()
      