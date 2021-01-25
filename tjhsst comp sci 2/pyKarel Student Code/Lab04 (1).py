#Name: Vivian and Karthik
#Date: 9/6/2019

from pyKarel import * 
from Athlete import Athlete

def takeTheField(arg):
   arg.turnLeft()
   arg.move()
   arg.move()
   arg.move()
   arg.move()
   arg.turnRight()
   arg.move()
   arg.move()
   
wld = World('arena')

coach = Athlete(wld, 2,7, east)

bob = Athlete(wld)
bob1 = Athlete(wld)
bob2 = Athlete(wld)
bob3 = Athlete(wld)
bob4 = Athlete(wld)
bob5 = Athlete(wld)

takeTheField(bob)
takeTheField(bob1)
takeTheField(bob2)
takeTheField(bob3)
takeTheField(bob4)
takeTheField(bob5)

bob.move()
bob.move()
bob.move()
bob.turnLeft()
bob.move()
bob.move()
bob.turnAround()

bob1.move()
bob1.turnLeft()
bob1.move()
bob1.turnAround()

bob2.move()
bob2.move()
bob2.turnRight()

bob3.move()
bob3.move()
bob3.move()
bob3.turnRight()

bob4.move()
bob4.move()
bob4.move()
bob4.move()
bob4.turnRight()

bob5.move()
bob5.move()
bob5.move()
bob5.move()
bob5.move()
bob5.turnLeft()
bob5.move()
bob5.turnAround()







wld.mainloop()



