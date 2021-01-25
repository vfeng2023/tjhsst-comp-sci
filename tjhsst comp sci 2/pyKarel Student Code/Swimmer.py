from Athlete import *

class Swimmer(Athlete):
   def __init__(self, wld, x):
      Athlete.__init__(self, wld, x)
      
      
   def swim_laps(self):
      for i in range(10):
         for k in range(8):
            self.move()
         self.turnAround()
      