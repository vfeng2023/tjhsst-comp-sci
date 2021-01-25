#Name: Vivian and Karthik

#Date: 10/18/2019

from PIL import Image

img = Image.new('RGB',(600,600),(0,0,0))

ptx1 = 0.05
pty1 = 0.05
ptx2= 0.95
pty2=0.05
ptx3 = 0.95
pty3 = 0.95
ptx4=0.05
pty4= 0.95



def drawLine(ptX1, ptY1, ptX2, ptY2):
  t = 0.0
  while t < 1.0:
    x = int (n * (ptX1 + t * (ptX2 - ptX1)))
    y = int (n * (ptY1 + t * (ptY2 - ptY1)))
    img.putpixel((x, y),(255, 204, 0)) # gold
    #
    t += 0.001