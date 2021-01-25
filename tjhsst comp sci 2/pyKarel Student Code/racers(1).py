#Name: Vivian and Karthik
#date: 9/6/2019

from pyKarel import *
from Athlete import Athlete

class Racer(Athlete):
   def __init__(self,world,y,d=east,beepers = 0):
      Athlete.__init__(self,world,1,y,d,beepers)
      
   def jumpEast(self):
      self.move()
      self.turnLeft()
      self.move()
      self.turnRight()
      self.move()
      self.turnRight()
      self.move()
      self.turnLeft()
      
   def jumpWest(self):
      self.move()
      self.turnRight()
      self.move()
      self.turnLeft()
      self.move()
      self.turnLeft()
      self.move()
      
   def sprint(self,n):
      for i in range(n):
         self.move()
         
   def put(self,n):
      for i in range(n):
         self.putBeeper()
         
   def pick(self,n):
      for i in range(n):
         self.pickBeeper()
         
         