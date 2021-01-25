
from Workers import *
from random import randint


def work_one_row(arg, m):
   for k in range(m):
      arg.doYourThing()
      arg.move()
      

def work_square(arg, n):
   n-=1
   arg.turnToTheNorth()
   work_one_row(arg, n)
   for k in range(n, 0, -1):
      arg.turnRight()
      work_one_row(arg, k)
      arg.turnRight()
      work_one_row(arg, k)
   arg.doYourThing()
   
   
   
   


def main():
   size = raw_input("Which 'field' (3,5,8)?")
   wld = World("field"+size, delay=0.1)
   if randint(0,1) == 0:
      work_square(Harvester(wld), int(size))
   else: 
      work_square(Planter(wld), int(size))
   
   wld.mainloop()
   
   
if __name__=="__main__":
   main()