# Name: Vivian Feng & Shriya Muthukumar
# Date: 2.18.2020

import Tkinter as tk

w,h = 600, 450
root = tk.Tk()
canvas = tk.Canvas(root, width = w, height = h)
canvas.pack()

minX,maxX = 2,4


x = 2.0

points = []
while x <= 4:
    oldY = 0.25
    for iteration in range(9100):
        newY = x*oldY * (1-oldY)

        coords = [x,newY]

        if iteration >= 9000:
            points.append(coords)

        oldY = newY
    x += 0.001

scaler = abs(w/(maxX-minX))

scaledPts = []
for point in points:
    scaledX = (point[0]-minX) * scaler
    scaledY = h-(point[1] * scaler)
    scaledPts.append([scaledX,scaledY])

for scaledPt in scaledPts:
    lowerScaledPt = [scaledPt[0]+1,scaledPt[1]+1]
    canvas.create_rectangle(scaledPt,lowerScaledPt,outline = 'black',fill='black')



root.mainloop()

