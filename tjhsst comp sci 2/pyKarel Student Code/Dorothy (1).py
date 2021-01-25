from pyKarel import *
from Athlete import *

class Dorothy(Athlete):
   def __init__(self,world):
      Athlete.__init__(self,world,2,2,east,0)
      
   def findPath(self):
         self.turnAround()
         self.move()
         self.turnAround()
         self.turnLeft()
         self.move()
         count = 0
         if self.nextToABeeper():
            self.move()
            count+= 1
         elif not self.nextToABeeper():      
            self.turnAround()
            self.move()
            self.move()
            if self.nextToABeeper():
               self.move()
            else:
               return False
         return True     
           
   def followPath(self):
      while self.nextToABeeper():
         if self.frontIsClear():
            self.move()
         else:
            self.turnLeft()
         
     
      
