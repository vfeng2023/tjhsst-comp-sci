from pyKarel import *
from Athlete import *

class Planter(Athlete):
   def __init__(self,world,x=2,y=2,direction=east,beepers = infinity):
      Athlete.__init__(self,world,x,y,direction,beepers)
      
   def doYourThing(self):
         
      if not self.nextToABeeper():
         self.putBeeper()
         
   def turnToTheNorth(self):
      while not self.facingNorth():
         self.turnLeft()
         
         
class Harvester(Athlete):
   def __init__(self,world,x=2,y=2,d=east,beepers=0):
      Athlete.__init__(self,world,x,y,d,beepers)
      
   def doYourThing(self):
      if self.nextToABeeper():
         self.pickBeeper()
      
   
   def turnToTheNorth(self):
      while not self.facingNorth():
         self.turnLeft()
