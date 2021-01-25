# Name: Vivian Feng and Shriya Muthukumar

from math import sqrt
# old x = 5
oldX = 5
# while x is not within margin of error to sqrt(2):
coords = open('lab20data.txt','w')
while abs(oldX - sqrt(2)) > 10**(-9):
#   new x = 0.5*(oldX+2/oldX)

    newX = 0.5*(oldX + (2.0/oldX))
#   write in file corners of of spiderweb plot
    coords.write(str(oldX)+ " "+str(oldX)+"\n")
    coords.write(str(oldX) + " " + str(newX)+"\n")

    oldX = newX

#       (old x, old x)
#       (old x, new x)
#       if first value, just write (old x, new x)

coords.close()
