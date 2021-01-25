#Name:
#Date:

from Athlete import *
   
class Dancer(Athlete):
    ## this class is abstract
    ## myDanceStep should be implemented in subclasses
    def dance(self):
         for k in range(1, 10):
            self.myDanceStep()


#  Define new classes here
    
