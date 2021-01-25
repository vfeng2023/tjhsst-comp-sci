#Name:
#Date:

from Mountain import *
from Climbers import *

def main():
    name_of_world = raw_input("Which 'mountain', 'hill', or 'step' world? ")
    kind_of_climber = raw_input("What kind of climber? ")
    x_coord = raw_input("What x-coordinate? ")    #reads a string
    x = int(x_coord)         # changes string to integer
    wld=World(name_of_world, width=20, height=10, delay=0.1)
   
    if  kind_of_climber == "Climber":
        reinhold_messner = Climber(wld,x)
    elif kind_of_climber == "HillClimber":
        reinhold_messner = HillClimber(wld,x)
    elif kind_of_climber == "StepClimber":
        reinhold_messner = StepClimber(wld, x)
    elif kind_of_climber == "Athlete":
        reinhold_messner = Athlete(wld, x)
    elif kind_of_climber == "Robot":
        reinhold_messner = Robot(wld, x)
    else:
        print("Invalid robot type.")
        sys.exit(0)         # exits gracefully, if needed
    explore(reinhold_messner)    
    wld.mainloop()

if __name__=="__main__":
    main()


