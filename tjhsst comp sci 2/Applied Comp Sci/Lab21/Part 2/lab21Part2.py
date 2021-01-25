# Name: Vivian Feng and Shriya Muthukumar
# Date: 2.14.2020

rValues = [2.9, 3.21, 3.5, 3.99]
# for each r value
for r in rValues:
    coords = open(str("r") + str(r).replace(".", "")+".txt", 'w')
    oldX = 0.25
    # create file
    iteration = 0
    while iteration < 400:
        newX = r * oldX * (1 - oldX)
        if iteration > 100:
            coords.write(str(oldX) + " " + str(oldX) + "\n")
            coords.write(str(oldX) + " " + str(newX) + "\n")
        oldX = newX
        iteration += 1
    coords.close()

# run x = r*x*(1-x) 400 times
# write for the last 300 times
