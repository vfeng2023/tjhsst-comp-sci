#name: Vivian Feng
#Date: 10/3/2019

import math

v0 = 26.82

angle = 30

c1 = float(raw_input("Give air resistance constant: ")) #c1=0 is also no air resistace parabola

vx = v0 * math.cos(angle * (math.pi/180))

vy = v0 * math.sin(angle * (math.pi/180))

x = 0

y = 0

g = -9.81 #set g as negative because in a system where up is positive and down is negative, 
          #g would be bringing velocity down 

dt = 0.001
xcoords,ycoords = [],[]
while y>=0:
   ax = (-c1*vx)
   ay = g-(c1*vy)
   vx += dt*ax
   vy += dt*ay
   x += vx*dt
   y += vy*dt
   xcoords.append(x)
   ycoords.append(y)

f = open('Lab04_'+str(c1)+'.txt','w')
for index in range(len(xcoords)):
   f.write(str(xcoords[index])+" "+str(ycoords[index])+"\n")
f.close()
