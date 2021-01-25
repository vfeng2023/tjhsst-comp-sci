#Name:
#Date:

from pyKarel import *

def explore(arg): 
    arg.putBeeper() 
    arg.turnLeft() 
    explore_west(arg) 
    if not arg.hasBeepers():
        explore_east(arg) 
    arg.pickBeeper()
    #wld.mainloop()

def explore_west(arg):
    n = 0 
    while arg.frontIsClear():
        arg.move() 
    while not arg.frontIsClear():
        arg.climbUpLeft() 
        n += 1 
    if arg.nextToABeeper():
        arg.pickBeeper() 
    arg.turnAround()
    for k in range(0, n):
        arg.climbDownRight() 
    while not arg.nextToABeeper():
        arg.move()
    #wld.mainloop()

def explore_east(arg):
    n = 0 
    while arg.frontIsClear():
        arg.move() 
    while not arg.frontIsClear():
        arg.climbUpRight() 
        n = n + 1 
    if arg.nextToABeeper():
        arg.pickBeeper() 
    arg.turnAround()
    for k in range(0, n):
        arg.climbDownLeft() 
    while not arg.nextToABeeper():
        arg.move() 

##END of FILE
