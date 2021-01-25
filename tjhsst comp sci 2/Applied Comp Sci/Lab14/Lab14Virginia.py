#Name: Vivian Feng and Karthik Bhurgav
#Date: 12/4/2019

from Tkinter import Tk,Canvas
#initalize canvas object
w,h = 640,480
root = Tk()
canvas = Canvas(root, width=w,height = h,bg='white')
canvas.pack()
#global mins and maxes
all_min_x,all_max_x = None,None
all_min_y,all_max_y = None,None

#adjust global mins and maxes
def find_min_max(coordinates):
   global all_min_x,all_max_x,all_min_y,all_max_y
   #gets x and y coordinates
   xcoords = [item[0] for item in coordinates]
   ycoords = [item[1] for item in coordinates]
   minx = min(xcoords)
   maxx = max(xcoords)
   miny = min(ycoords)
   maxy = max(ycoords)
   #sets maxes and mins
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
def plot_figure(coordinates,canvas):
   #finds optimal scaler that fills screen and preserves shape
   scaler =  min([w/(all_max_x-all_min_x),h/(all_max_y-all_min_y)])*0.9
   
   for coordinate in range(len(coordinates)):
      coordinates[coordinate][0] = ((coordinates[coordinate][0])-all_min_x)*scaler
      coordinates[coordinate][1] = h-((coordinates[coordinate][1])-all_min_y)*scaler
   
   
   dc = canvas.create_polygon(coordinates,fill = 'gray',outline = 'black')
   canvas.move(dc,(w-all_max_x)*0.25,0)
   
#open file   
file = 'tangier_island.txt'
state_coords = open(file,'r')
#get coordinates of alabama
contents = state_coords.readlines()
all_coords = []
coords = []

# va_index = contents.index('VA\n')
# va_coords = open('va_coords.txt','w')
for line in contents:
   if line.strip() == 'VA':
      continue
      
   elif line.strip() == 'END_ONE_POLY':
      all_coords.append(coords)
         
      coords = []
      continue
         
   elif line.strip() == 'END_ALL_POLY':
      break
         
   else: 
      coordstr = line.split()
      floatcoords = list(map(float,coordstr))
      coords.append(floatcoords)
      

         

find_min_max(coords)
   

plot_figure(coords,canvas)
   
root.mainloop()
   