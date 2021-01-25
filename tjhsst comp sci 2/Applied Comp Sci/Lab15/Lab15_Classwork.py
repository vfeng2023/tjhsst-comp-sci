##Name: Vivian Feng and Karthik Bhargav
#Date: 1/6/2020

from Tkinter import *
from random import randint

w,h = 600,600
root = Tk()
cnvs = Canvas(root, width=w,height = h,bg='white')
cnvs.pack()


#Initalize 1000 pts
for point in range(1000):
   cnvs.create_rectangle(w/2.0, h/2.0 ,w/2.0 + 1, h/2.0 + 1,fill='black',outline='black')


#Define tick function
def tick():
   #For each point, use randInt to choose a direction to move
   #1 = up
   #2 left
   #3 right
   #4 down
   for x in range(1000):
      coin = randint(1,4)
      if coin == 1:
         cnvs.move(x,0,1)
      
      elif coin == 2:
         cnvs.move(x,-1,0)
         
      elif coin == 3:
         cnvs.move(x,1,0)
         
      else:
         cnvs.move(x,0,-1)

   #Move
   cnvs.after(1,tick)
   #Stop at a timestep
   
cnvs.after(100,tick)
root.mainloop()
   
