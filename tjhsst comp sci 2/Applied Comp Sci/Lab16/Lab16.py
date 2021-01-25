#Name: Vivian and Karthik
#Date: ...

from random import randint
from Tkinter import Tk,Canvas
from math import sqrt

#initiate canvas
root = Tk()
w,h=600,600
canvas = Canvas(root,width=w,height=h,bg='white')
canvas.pack()
#records amount of steps taken
timeStep = 0
#open file to record data
dist_data = open('lab16data.txt','w')
#create points
for point in range(1000):
   canvas.create_rectangle(w/2-1,h/2-1,w/2+1,h/2-1,fill='black',outline='black')

#move points randomly
def move_point():
#repeat large number of times, stoping at 5000 iterations
   global timeStep
   if timeStep <=5000:
      ptDists = []
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
         pointcoords = canvas.coords(point_id)
         #calculate and append distances
         if len(pointcoords) == 4:
            x1,y1,x2,y2 = tuple(pointcoords)
            pointCentX = (x1+x2) * 0.5
            pointCentY = (y1+y2) * 0.5
            ptDists.append(calc_dist(pointCentX,pointCentY,w/2,h/2))
            
      #calculate averages
      arithAvg = calc_avg(ptDists)
      rmsAvg = find_rms(ptDists)
      #write in data file
      dist_data.write(str(timeStep) + " " + str(arithAvg) + " " + str(rmsAvg)+ "\n")  
      timeStep += 1
   
      canvas.after(1,move_point)


def calc_dist(x1,y1,x2,y2):
   """This function finds the distance between two points"""
   xChange = x2-x1
   yChange = y2-y1
   pythag = xChange**2 + yChange**2
   return sqrt(pythag)
 
#find arithemetic mean
def calc_avg(nums):
   return sum(nums)/len(nums)

#find rms
def find_rms(distList):
   squaredSum = 0
   for dist in distList:
      squaredSum += dist
   rms = sqrt(squaredSum/len(distList))
   return rms
  
canvas.after(1,move_point)

root.mainloop()