#Name:Karthik and Vivian
#Date:09/04/2019

from pyKarel import *

from Athlete import *

class Climber(Athlete):
   def __init__(self,world,x,y=1,direction=north,beepers = 1):
      Athlete.__init__(self,world,x,y,direction,beepers)
   
   def climbUpRight(self):
      self.turnLeft()
      self.move()
      self.move()
      self.turnRight()
      self.move()
      
      
      
   def climbDownRight(self):
      self.move()
      self.turnRight()
      self.move()
      self.move()
      self.turnLeft()
      
   def climbUpLeft(self):
      self.turnRight()
      self.move()
      self.move()
      self.turnLeft()
      self.move()
      
   def climbDownLeft(self):
      self.move()
      self.turnLeft()
      self.move()
      self.move()
      self.turnRight()

   
      
     
