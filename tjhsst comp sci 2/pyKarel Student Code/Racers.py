#Name: Vivian and Karthik
#date: 9/6/2019

from pyKarel import *
from Athlete import Athlete

class Racer(Athlete):
   def __init__(self,world,y,d=east,beepers = 0):
      Athlete.__init__(self,world,1,y,d,beepers)
      
   def jumpEast(self):
      self.turnLeft()
      self.move()
      self.turnRight()
      self.move()
      self.turnRight()
      self.move()
      self.turnLeft()
      
   def jumpWest(self):

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

class SteepleChaseRacer(Racer):
   def __init__(self,world,y):
      Racer.__init__(self,world,y)

   def jumpEast(self):
      self.turnLeft()
      while self.rightIsClear() == False:
         self.move()
      self.turnRight()
      self.move()
      self.turnRight()
      
      while self.frontIsClear():
         self.move()
         
      self.turnLeft()

class BoxTopRacer(Racer):
   def __init__(self,world,y):
      Racer.__init__(self,world,y)

   def jumpEast(self):
      self.turnLeft()
      while not self.rightIsClear():
         self.move()
      self.turnRight()
      self.move()
      while not self.rightIsClear():
         self.move()

      self.turnRight()
      while self.frontIsClear():
         self.move()
  

      self.turnLeft()
      
   
         
