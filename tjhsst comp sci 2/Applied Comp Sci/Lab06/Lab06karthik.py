##Name: Karthik and Vivian
##Date: 10/04/2019

import math

v0 = 0.0

theta = math.pi/2

vw = 0.44704

c1 = 0.5

vx = v0 * math.cos(theta)#Just demonstrated in Radians
vy = v0 * math.sin(theta)#In Radians

x=0 #Meters
y=1500.0 #Defined in Meters
g = -9.81#Gravity
#Up is Positive, Down is Negative

t=0

dt = 0.01

j = open('Lab06.txt','w')#Connects the Air Resistance to w#Listed created to have the X and Y coordinates
while y>=0.0:
   ax = -c1*(vx-vw)#Horizontal Acceleration
   ay=(g-c1*vy)#Vertical Acceleration
   x+=(vx*dt)
   y+=(vy*dt)
   vx+=(ax*dt)#Velocity X
   vy+=(ay*dt)#Y
   t+=dt
   
   
   j.write(str(t) + " "+str(x)+ " " + str(y)+ " " + str(vx)+ " " + str(vy)+ " "+ str(ax)+ " "+ str(ay)+ " " + "\n") #Connects the x and y coordinates, uses Index(In this case i) to put in the Lab04 file
   
      
j.close()   
   
