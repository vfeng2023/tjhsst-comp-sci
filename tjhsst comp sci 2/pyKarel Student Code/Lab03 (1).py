#Name:Karthik and Vivian
#Date: 9/4/2019

from pyKarel import *
from Athlete import *
from Climber import Climber

wld = World('mountain',height =8,width=16)


t = Climber(wld, 8,1, north, 1)
r= Climber(wld, 8,1, north, 1)

r.putBeeper()
r.turnRight()
t.turnRight()
r.move()
t.move()
r.turnLeft()
t.turnLeft()
r.climbUpRight()
t.climbUpRight()
r.climbUpRight()
t.climbUpRight()
r.climbUpRight()
t.climbUpRight()
t.turnRight()
r.turnRight()
t.climbDownRight()
r.climbDownRight()
t.climbDownRight()
r.climbDownRight()
r.pickBeeper()
r.turnAround()
t.turnAround()
t.climbUpLeft()
r.climbUpLeft()
t.climbUpLeft()
r.climbUpLeft()
t.climbDownLeft()
r.climbDownLeft()
t.climbDownLeft()
r.climbDownLeft()
t.climbDownLeft()
r.climbDownLeft()
t.move()
r.move()
t.putBeeper()
r.move()
t.move()

wld.mainloop()
