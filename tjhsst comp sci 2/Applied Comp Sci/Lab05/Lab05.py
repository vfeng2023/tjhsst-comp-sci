#name: Vivian Feng
#Date: 10/3/2019

import math
inpu = raw_input("Option 1 or Option 2: ")
#Option 1 is for the effect of windspeed for distance vs height graphs
#Option 2 is for windspeed vs range graphs
if inpu == "1":
   v0 = 15.00
   
   angle = 60
   
   c1 = 0.5 #supposed to be 0.5
   
   vx = v0 * math.cos(angle * (math.pi/180))
   
   vy = v0 * math.sin(angle * (math.pi/180))
   
   vw = float(raw_input("Give speed of wind: ")) 
   x = 0
   
   y = 0
   
   g = -9.81 #set g as negative because in a system where up is positive and down is negative, 
             #g would be bringing velocity down 
   
   dt = 0.001
   xcoords,ycoords = [],[]
   while y>=0:
      ax = -c1*(vx-vw)
      ay = g-(c1*vy)
      vx += dt*ax
      vy += dt*ay
      x += vx*dt
      y += vy*dt
      xcoords.append(x)
      ycoords.append(y)
   
   f = open('Lab05_'+str(vw)+'.txt','w')
   for index in range(len(xcoords)):
      f.write(str(xcoords[index])+" "+str(ycoords[index])+"\n")
   f.close()

else:
   xaxis = [i for i in range(-10,31)]
   yaxis = []
   for vw in range(-10,31):
      v0 = 15.00
      
      angle = 60
      
      c1 = 0.5 #supposed to be 0.5
      
      vx = v0 * math.cos(angle * (math.pi/180))
      
      vy = v0 * math.sin(angle * (math.pi/180))
 
      x = 0
      
      y = 0
      
      g = -9.81 #set g as negative because in a system where up is positive and down is negative, 
                #g would be bringing velocity down 
      
      dt = 0.001
      xcoords,ycoords = [],[]
      while y>=0:
         ax = -c1*(vx-vw)
         ay = g-(c1*vy)
         vx += dt*ax
         vy += dt*ay
         x += vx*dt
         y += vy*dt
         
      yaxis.append(x)
   f = open("Lab05vwvsrange.txt",'w')
   for j in range(len(xaxis)):
      f.write(str(xaxis[j]) + " "+ str(yaxis[j])+"\n")
