#Name: Vivian
#Date: 8/26/2019

from pyKarel import *

wld = World("first")
karel = Robot(wld)

karel.move()
karel.pickBeeper()
karel.move()
karel.turnLeft()
karel.move()
karel.putBeeper()
karel.move()
karel.turnLeft()
karel.turnLeft()
wld.mainloop()

