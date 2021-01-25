# Name:
# Date:

from pyKarel import *
from Dorothy import *

def main():       
    name_of_world=raw_input("Which 'yellow brick' path? ")
    wld=World(name_of_world, width=10, height=10, delay=0.1)
    d = Dorothy(wld)
    complete = True
    while True:
       d.followPath()
       d.findPath()
       
       
    
    print "We're not in Kansas anymore..."
    wld.mainloop()
    
if __name__=="__main__":
   main()
