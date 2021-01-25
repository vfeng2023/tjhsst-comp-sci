#Name:
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

# define more segments, both on and off




##------------------------------------------------        
class Zero(Digit):     
    def showMyDigit(self):
        self.segment1_On();
        self.segment2_On();
        self.segment3_On();
        self.segment4_On();
        self.segment5_On();
        self.segment6_On();
        self.segment7_Off();
##------------------------------------------------
# define other digit classes here


 
