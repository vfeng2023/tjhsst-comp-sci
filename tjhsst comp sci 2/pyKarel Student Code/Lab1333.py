#Name: Karthik and Vivian
#Date: 11/15/2019

from Tkinter import Tk,Canvas


w,h=640,480

root=Tk()
cnvs=Canvas(root,width=w,height=h,bg='white' ) 
cnvs.pack()

#read data
dccoords = open("lab312.txt",'r').read()
coords = dccoords.split()

coordinates = []
i=0
while i < len(coords):
   coordinates.append([float(coords[i]),float(coords[i+1])])
   i = i+2
print(coordinates)
print

#increase differences in coordinates
for index in range(len(coordinates)):
   coordinates[index][0] = (-1*coordinates[index][0])*9
   coordinates[index][1] = (coordinates[index][1])*18
   
print(coordinates)
print
#scaling for canvas
scaler = 0.25
for coordinate in range(len(coordinates)):
   #adjust aspect ratio
   coordinates[coordinate][0] =( 640-(((coordinates[coordinate][0]*640) - 443000) * scaler+250))*1.3
   coordinates[coordinate][1] = 480-(((coordinates[coordinate][1]*480) - 336000) * scaler+230)
print(coordinates)
print   

dc = cnvs.create_polygon(coordinates,fill = 'gray',outline = 'black')



root.mainloop()
   
   