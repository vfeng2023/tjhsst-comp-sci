#Name:Vivian and Karthik
#Date:

from Athlete import *

class Digit(Athlete):
   def __init__(self, world, x, y):
      Athlete.__init__(self, world, x, y, east, infinity)

   def display(self):
        ## this method is abstract
        ## showMyDigit() should be implemented in subclasses
      self.showMyDigit()

   def threeNoTurn(self, on):
      for x in range(3):
         self.move() 
         if(on):
            self.putBeeper()
      self.move() 
     
   def threeAndTurn(self, on):
      self.threeNoTurn(on) 
      self.turnRight()
    
   def segment1_On(self):
      self.threeAndTurn(True)

   def segment1_Off(self):
      self.threeAndTurn(False)
        
   def segment2_On(self):
      self.threeNoTurn(True)
    
   def segment2_Off(self):
      self.threeNoTurn(False)
    
   def segment3_On(self):
      self.threeAndTurn(True)
    
   def segment3_Off(self):
      self.threeAndTurn(False)
     
   def segment4_On(self):
      self.threeAndTurn(True)
    
   def segment4_Off(self):
      self.threeAndTurn(False) 
       
   def segment5_On(self):
      self.threeNoTurn(True)
    
   def segment5_Off(self):
      self.threeNoTurn(False)
     
   def segment5_On(self):
      self.threeNoTurn(True)
    
   def segment5_Off(self):
      self.threeNoTurn(False)

   def segment6_On(self):
      self.threeNoTurn(True)
    
   def segment6_Off(self):
      self.threeNoTurn(False)
      
   def segment7_On(self):
      self.turnAround()
      self.threeNoTurn(False)
      self.turnLeft()
      self.threeAndTurn(True)
      
   def segment7_Off(self):
      self.turnAround()
      self.threeNoTurn(False)
      self.turnLeft()
      self.threeAndTurn(False)


##------------------------------------------------        
class Zero(Digit):     
   def showMyDigit(self):
      self.segment1_On()
      self.segment2_On()
      self.segment3_On()
      self.segment4_On()
      self.segment5_On()
      self.segment6_On()
      self.segment7_Off()
##------------------------------------------------
# define other digit classes here

class One(Digit):
   def showMyDigit(self):
      self.segment1_Off()
      self.segment2_Off()
      self.segment3_Off()
      self.segment4_Off()
      self.segment5_On()
      self.segment6_On()
      self.segment7_Off()
      
class Five(Digit):
   def showMyDigit(self):
      self.segment1_On()
      self.segment2_Off()
      self.segment3_On()
      self.segment4_On()
      self.segment5_Off()
      self.segment6_On()
      self.segment7_On()

class Three(Digit):
   def showMyDigit(self):
      self.segment1_On()
      self.segment2_On()
      self.segment3_On()
      self.segment4_On()
      self.segment5_Off()
      self.segment6_Off()
      self.segment7_On()

class Nine(Digit):
   def showMyDigit(self):
      self.segment1_On()
      self.segment2_On()
      self.segment3_On()
      self.segment4_On()
      self.segment5_Off()
      self.segment6_On()
      self.segment7_On()

class Eight(Digit):
   def showMyDigit(self):
      self.segment1_On()
      self.segment2_On()
      self.segment3_On()
      self.segment4_On()
      self.segment5_On()
      self.segment6_On()
      self.segment7_On()
      
class Two(Digit):
   def showMyDigit(self):
      self.segment1_On()
      self.segment2_On()
      self.segment3_Off()
      self.segment4_On()
      self.segment5_On()
      self.segment6_Off()
      self.segment7_On()