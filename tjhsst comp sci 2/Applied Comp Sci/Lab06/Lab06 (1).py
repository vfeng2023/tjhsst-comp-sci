#Name: Karthik and Vivian
#Date: 10/3/2019

import math

c1=0.5 #air resistance

v0 = 0.0 #initial velocity

vw = 0.44704 # windspeed

theta = 90

vx = 0
vy = 0

x = 0.0 #distance

y = 1500.0 #height

t = 0 #time that has passed

g = -9.81
dt = 0.01 # uses larger timestep to avoid excel lagging out

f = open('lab06data.txt','w')
#t ax ay vx vy x y
while y>0: # makes necessary changes to conditions
   ax = -c1 *(vx-vw)
   ay = g-c1*vy
   vx += dt*ax
   vy += dt*ay
   t+=dt
   x+= dt*vx
   y+= dt*vy
   f.write(str(t) + " " + str(ax) + " "+ str(ay) +" "+str(vx) + " "+str(vy)+ " "+ str(x)+" "+str(y)+"\n")
   
f.close()