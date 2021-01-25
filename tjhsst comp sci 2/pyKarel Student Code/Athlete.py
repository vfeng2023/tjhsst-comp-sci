#Name: Vivian and Karthik
#Date: 8/28/2019

from pyKarel import *
class Athlete(Robot):
   def turnRight(self):
      for i in range(3):
         self.turnLeft()
         
   def turnAround(self):
      self.turnLeft()
      self.turnLeft()
   
      