# Name:
# Date:

from pyKarel import *
from Dorothy import *
def main():       
    name_of_world=raw_input("Which 'yellow brick' path? ")
    wld=World(name_of_world, width=10, height=10,)
    d = Dorothy(wld)
    complete = True
    while complete:
       d.followPath()
       complete = d.findPath()
    d.turnAround()   
    for i in range(4):
      d.move()
      d.turnLeft()   
    d.move()
    d.turnRight()
    print "We're not in Kansas anymore..."
    wld.mainloop()
    
if __name__=="__main__":
   main()
