#Name: Vivian and Karthik
#date: 9/6/2019

from pyKarel import *
from racers import Racer

wld = World("shuttle")

r1 = Racer(wld,1)
r2 = Racer(wld,4)
r3 = Racer(wld,7)

def runTheRace(arg):
   arg.jumpEast()
   arg.sprint(2)
   arg.pick(7)
   arg.sprint(2)
   arg.pick(5)
   arg.sprint(2)
   arg.pick(3)
   arg.turnAround()
   arg.sprint(5)
   arg.jumpWest()
   arg.turnRight()
   arg.move()
   arg.put(15)
   arg.turnAround()
   arg.move()
   
for racer in [r1,r2,r3]:
   runTheRace(racer)
   
   
wld.mainloop()