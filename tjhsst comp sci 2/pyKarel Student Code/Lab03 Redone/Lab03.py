#Name:Karthik and Vivian
#Date: 9/4/2019

from pyKarel import *
from Climber import Climber
wld = World('mountain',height =8,width=16)


t = Climber(wld, 8,1, north, 1)
r= Climber(wld, 8,1, north, 1)

r.putBeeper()
r.turnRight()
t.turnRight()
r.move()
t.move()
r.climbUpRight()
t.climbUpRight()
r.climbUpRight()
t.climbUpRight()
r.climbUpRight()
t.climbUpRight()
r.turnRight()
t.turnRight()
r.climbDownRight()
t.climbDownRight()
r.climbDownRight()
t.climbDownRight()
r.pickBeeper()
t.turnAround()
r.turnAround()
t.move()
t.move()
r.move()
r.move()
t.climbUpLeft()
r.climbUpLeft()
t.turnLeft()
t.move()
t.move()
r.turnLeft()
r.move()
r.move()
t.climbDownLeft()
r.climbDownLeft()
t.climbDownLeft()
r.climbDownLeft()
t.climbDownLeft()
r.climbDownLeft()
t.putBeeper()
r.move()
t.move()




wld.mainloop()