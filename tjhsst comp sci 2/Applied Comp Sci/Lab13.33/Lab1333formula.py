#Name: Karthik and Vivian
#Date: 11/15/2019

from Tkinter import Tk,Canvas


w,h=640,480

root=Tk()
cnvs=Canvas(root,width=w,height=h,bg='white' ) 
cnvs.pack()

dccoords = open("lab312.txt",'r')

coords = dccoords.readlines()
all_min_x,all_max_x = None,None
all_min_y,all_max_y = None,None
#read data
coordinates = []
for coord in coords:
   coordstr = coord.split()
   floatcoords = list(map(float,coordstr))
   coordinates.append(floatcoords)
print(coordinates)      

#find global mins and maxes
def find_min_max(coordinates):
   global all_min_x,all_max_x,all_min_y,all_max_y
   #gets x and y coordinates
   xcoords = [item[0] for item in coordinates]
   ycoords = [item[1] for item in coordinates]
   minx = min(xcoords)
   maxx = max(xcoords)
   miny = min(ycoords)
   maxy = max(ycoords)
   if (all_min_x == None) or all_min_x > minx:
      all_min_x = minx
      
   if (all_max_x == None) or all_max_x < minx:
      all_max_x = maxx
   
   if (all_min_y == None) or all_min_y > miny:
      all_min_y = miny
      
   if (all_max_y == None) or all_max_y < miny:
      all_max_y = maxy     
   print 'maxes and mins:',all_min_x,all_max_x,all_min_y,all_max_y
#scaling for canvas
def plot_figure(coordinates,cnvs):
   #finds optimal scaler that fills screen and preserves shape
   scaler =  min([w/(all_max_x-all_min_x),h/(all_max_y-all_min_y)])*0.9
   
   for coordinate in range(len(coordinates)):
      coordinates[coordinate][0] = ((coordinates[coordinate][0])-all_min_x)*scaler 
      coordinates[coordinate][1] = h-(coordinates[coordinate][1]-all_min_y)*scaler
   
   
   maxxp = max([item[0] for item in coordinates])

   print(maxxp)
   print((w-maxxp)/2)
   dc = cnvs.create_polygon(coordinates,fill = 'gray',outline = 'black')
   cnvs.move(dc,(w-maxxp)/2,0)
   

find_min_max(coordinates)
plot_figure(coordinates,cnvs)
root.mainloop()
   
   