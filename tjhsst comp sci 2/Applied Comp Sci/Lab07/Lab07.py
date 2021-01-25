#Name: Vivian Feng and Karthik Bhargav
#Date" 10/9/2019

from PIL import Image

size = int(raw_input("Size of Circle: "))

if size == 600:
   qc = Image.new('RGB',(600,600),(143,154,255))
   
   yp = 0
   qcpixels = 0
   
   while yp < 600:
      xp = 0
      while xp < 600:
         x = (xp+0.5)/600
         y = (yp+0.5)/600
         if (x**2) + (y**2) <= 1:
            qc.putpixel((xp,yp),(145,145,145))
            qcpixels += 1
         xp+=1
      yp += 1
   
   qc.save('quarter_circle.png')
   Image.open('quarter_circle.png')
     
   api = qcpixels/(600.0**2)
   
   print "Pi approximation: ",4*api
   
else:
   
   yp = 0
   qcpixels = 0
   
   while yp < size:
      xp = 0
      while xp < size:
         x = (xp+0.5)/size
         y = (yp+0.5)/size
         if (x**2) + (y**2) <= 1:
            qcpixels += 1
         xp+=1
      yp += 1
        
   api = qcpixels/(float(size)**2)

   print "Approximation of pi:",4*api
