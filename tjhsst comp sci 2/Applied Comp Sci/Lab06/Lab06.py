#Name: ... and Vivian
#Date: 10/3/2019

import math

c1=0.5 #air resistance

v0 = 0.0 #initial velocity

vw = 0.44704 # windspeed

theta = math.pi/2

vx = v0* math.cos(theta)
vy = v0 * math.sin(theta)

x = 0.0 #distance

y = 1500.0 #height

t = 0 #time that has passed

g = -9.81
dt = 0.001
while y>0:
   ax = -c1 *(vx-vw)
   ay = g-c1*vy
   vx = dt*ax
   vy = dt*ay
   t+=dt
   
   f = 
   
