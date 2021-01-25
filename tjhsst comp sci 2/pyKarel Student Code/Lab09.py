#Name: Vivian and Karthik
#Date: 9/13/2019


from pyKarel import *
from Athlete import *

wld_choice = raw_input("Which world? ")
wld = World(wld_choice,height=3,width=8)
a = Athlete(wld,1,1,east,0)

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

countlist = [count1,count2,count3,count4,count5,count6,count7]
for i in range(7):
   x = 0
   while a.nextToABeeper():
      a.pickBeeper()
      x+=1
   countlist[i] = x
   a.move()
                           
   
a.turnAround()
for j in range(7):
   a.move()

a.turnAround()
a.move()
for count in countlist:
   for g in range(count):
      a.putBeeper()
   a.move()

wld.mainloop()
