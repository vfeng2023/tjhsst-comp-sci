#Name:
#Date:

from Racers import *

def race(arg):
    while not arg.nextToABeeper():
        if arg.frontIsClear():
          arg.move()  
        else:
          arg.jumpEast()  
          
def main():
    name_of_world = raw_input("Which 'hurdle', 'steeple', or 'boxtop' world? ")
    kind_of_racer = raw_input("What kind of racer? ")

    wld=World(name_of_world, width=20, height=10, delay=0.1)
   
    if  kind_of_racer == "Racer":
        jesse_owens = Racer(wld,1)
    elif kind_of_racer == "SteepleChaseRacer":
        jesse_owens = SteepleChaseRacer(wld,1)
    elif kind_of_racer == "BoxTopRacer":
        jesse_owens = BoxTopRacer(wld,1)
    elif kind_of_racer == "Athlete":
        jesse_owens = Athlete(wld)
    elif kind_of_racer == "Robot":
        jesse_owens = Robot(wld)
    else:
        print("Invalid robot type.")
        sys.exit(0)
    race(jesse_owens)    
    wld.mainloop()

if __name__=="__main__":
   main()

##  End of file
