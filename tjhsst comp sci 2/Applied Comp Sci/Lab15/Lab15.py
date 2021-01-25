#Name: Vivian and Karthik
#Date: ...

from random import randint
from Tkinter import Tk,Canvas
#initiate canvas
root = Tk()
w,h=600,600
canvas = Canvas(root,width=w,height=h,bg='white')
canvas.pack()

#create points
for point in range(1000):
   canvas.create_rectangle(w/2-1,h/2-1,w/2+1,h/2-1,fill='black',outline='black')

#move points randomly
def move_point():
   for point_id in range(1000):
      result = randint(1,4)
      if result == 1:
         canvas.move(point_id,-1,0)
         
      elif result == 2:
         canvas.move(point_id,0,1)
         
      elif result == 3:
         canvas.move(point_id,1,0)
         
      else:
         canvas.move(point_id,0,-1)

   #repeat large number of times
   canvas.after(1,move_point)
   
canvas.after(100,move_point)

root.mainloop()