# Name: Vivian Feng and Shriya Muthukumar
# Date: 2.14.2020

# open file
coords = open('lab21part1.txt', 'w')

# repeat 20 times:
oldX = 3.7
for iteration in range(20):
    newX = 1.0/(4-oldX)
    coords.write(str(oldX) + " " + str(oldX) + "\n")
    coords.write(str(oldX) + " "+ str(newX) + "\n")
    oldX = newX

coords.close()
#   x(n) = 1/(4-x(n-1)),
#   (oldX,oldX)
#   (oldX, newX)

