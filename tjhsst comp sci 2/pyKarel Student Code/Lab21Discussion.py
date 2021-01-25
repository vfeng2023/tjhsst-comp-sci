
# Name:  
# Date:  

from pyKarel import *
from Athlete import *

def recur(arg):
    if arg.nextToABeeper():    # base case
        arg.pickBeeper()
        arg.turnLeft()
    else:
        arg.move()
        recur(arg)             # recursive call
        arg.move()             # this command is stored; eventually it is executed
 

def main():     
    wld = World("Lab21Discussion")
    karel = Athlete(wld, 1,1,east, 0)

## Iterative solution    
    count = 0
    while not karel.nextToABeeper():
        karel.move()
        count = count + 1
    karel.pickBeeper()
    karel.turnLeft()
    for k in range (count):
       karel.move()
    karel.putBeeper()
    wld.mainloop()

## Recursive solution
##    recur(karel)
##    karel.putBeeper()
##    wld.mainloop()
    



if __name__=="__main__":
   main()
