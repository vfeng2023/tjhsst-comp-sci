#Name: Vivian Feng and Karthik

from Tkinter import Tk,Canvas
from PIL import Image,ImageTk

w,h = 800,600

g = -1.6
dt =0.05
y=100.0
vy =0.0
t = 0.0

def tick():
   global y,vy,t
   
   y+= (vy*dt)
   vy += (g*dt)
   t += dt
   print t,y,vy
   
   yp=0.7*h -0.7*h*y/100.0
   canvas.coords(ship,w/4,yp)
   
   if y>=0.0:
      canvas.after(1,tick)
      
      
root = Tk()
canvas = Canvas(root,width=w,height=h,bg='black')
canvas.pack()

img1 = Image.open('earthrise.jpg').resize((w,h))
pmg1 = ImageTk.PhotoImage(img1)
canvas.create_image(w/2,h/2,image=pmg1)

img2 = Image.open('eagle.jpg').resize((200,200))
pmg2 = ImageTk.PhotoImage(img2)
ship=canvas.create_image(w/4,0,image=pmg2)

canvas.create_rectangle(w/4-150,int(0.5+0.7*h)+100,w/4+150,int(0.5+0.7*h)+125,outline = 'green',fill = 'green')

print t,y,vy

canvas.after(1000,tick)
root.mainloop()

