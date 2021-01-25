#Name: Vivian and Karthik
#date: 9/6/2019

from pyKarel import *
from racer import Racer
from threading import Thread

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
   
t1 = Thread(target=runTheRace,args=(r1,))
t2 = Thread(target=runTheRace,args=(r2,))
t3 = Thread(target=runTheRace,args=(r3,))  

t1.start()
t2.start()
t3.start()
   
wld.mainloop()