#Name: Karthik Bhargav and Vivian Feng
#Date: 11/25/2019

from Tkinter import Tk,Canvas
#read data
data_file = open('lab313.txt').read()
data = data_file.split()
all_coords = []
curr_coords = []
index = 0
while index < len(data):
   x = data[index]
   y = data[index]
   
   try:
      point = [float(x),float(y)]
      
   except ValueError:
      if len(x) != 2:
         all_coords.append(curr_coords)
         curr_coords = []
         index += 1
   else:
      curr_coords.append(point)
      index += 2
print('done')      
data_file.close()
#resize
scaler = 1         
for coord_set in range(len(all_coords)):
   for coord_index in range(len(all_coords[coord_set])):
      all_coords[coord_set][coord_index][0] = all_coords[coord_set][coord_index][0] * scaler
      all_coords[coord_set][coord_index][1] = all_coords[coord_set][coord_index][1] * scaler
   
   
#plot
root = Tk()
canvas = Canvas(root,width = 640,height = 480)

for mod_coords in range(len(all_coords)):
   canvas.create_polygon(all_coords[mod_coords],fill = 'gray')
   
for i in range(2):
   canvas.move(i,1,1)
   
root.mainloop()