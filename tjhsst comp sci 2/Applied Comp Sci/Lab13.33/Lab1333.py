#Name: Karthik and Vivian
#Date: 11/15/2019

from Tkinter import Tk,Canvas


w,h=640,480

root=Tk()
cnvs=Canvas(root,width=w,height=h,bg='white' ) 
cnvs.pack()

dccoords = open("lab312.txt",'r')

coords = dccoords.readlines()

#read data
coordinates = []
for coord in coords:
   coordstr = coord.split(" ")
   coordfloat = []
   for co in coordstr:
      coordfloat.append(float(co))
   coordinates.append(coordfloat)
   
print(coordinates)
print
   
#get 1 x 1 coordinates
for index in range(len(coordinates)):
   coordinates[index][0] = (coordinates[index][0]+0.5)/180
   coordinates[index][1] = (coordinates[index][1]+0.5)/360
   
print(coordinates)
print
#scaling for canvas
for coordinate in range(len(coordinates)):
   coordinates[coordinate][0] = (-1*coordinates[coordinate][0]*640)*5
   coordinates[coordinate][1] = (coordinates[coordinate][1]*480)*5
print(coordinates)
print   
cnvs.create_polygon(coordinates,fill = 'gray',outline = 'black')

root.mainloop()
   
   