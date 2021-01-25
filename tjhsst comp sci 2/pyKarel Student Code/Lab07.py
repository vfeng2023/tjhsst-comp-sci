#name:
#date:

from Pirate import *

def main():       
   name_of_world=raw_input("Which 'treasure map'? ")
   wld=World(name_of_world, width=8, height=8, delay=0.1)

   karel = Pirate(wld) 
   totalBeepers = 0 
   numOfBeepers = 0 
   while numOfBeepers != 5:
      karel.approachPile() 
      numOfBeepers = karel.numOfBeepersInPile() 
      totalBeepers += numOfBeepers 
      if numOfBeepers != 5:
         karel.turnAppropriately(numOfBeepers) 
   print "Total beepers: ", totalBeepers
   wld.mainloop()


if __name__=="__main__":
   main()
