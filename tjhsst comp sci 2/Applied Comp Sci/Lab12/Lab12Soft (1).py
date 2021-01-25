#Name: Vivian Feng and Karthik

from Tkinter import Tk,Canvas
from PIL import Image,ImageTk

w,h = 800,600

g = -1.6
dt =0.05
y=100.0
vy =0.0
t = 0.0
space_count = 0
f_obj = open('Lab12Soft.txt','w')
def tick():
   global y,vy,t
   
   y+= (vy*dt)
   vy += (g*dt)
   t += dt
   f_obj.write(str(t) + " " + str(y) + " "+ str(vy) +'\n')
   canvas.itemconfigure(txt,text='%0.2f'%vy) #change txt object
   #changes fuel bar
   canvas.itemconfigure(fuel_bar,text=str(20-space_count))
   #updates height
   yp=0.7*h -0.7*h*y/100.0
   canvas.coords(ship,w/4,yp)
   
   #reduces speed
   if y < 8:
      space()
   if y>=0.0:
      canvas.after(1,tick)
#thrust      
def space():
   global vy,space_count
   if space_count < 20:
      vy += 1
      space_count += 1
   
root = Tk()
canvas = Canvas(root,width=w,height=h,bg='black')
canvas.pack()


#creates background
img1 = Image.open('earthrise.jpg').resize((w,h))
pmg1 = ImageTk.PhotoImage(img1)
canvas.create_image(w/2,h/2,image=pmg1)

#opens eagle.jpg
img2 = Image.open('eagle.jpg').resize((200,200))
pmg2 = ImageTk.PhotoImage(img2)
ship=canvas.create_image(w/4,0,image=pmg2)

#creates landing pad
canvas.create_rectangle(w/4-150,int(0.5+0.7*h)+100,w/4+150,\
int(0.5+0.7*h)+125,outline = 'green',fill = 'green')

f=('Times',36,'bold')
txt=canvas.create_text(w-100,50,text='0.0',font=f,fill='white') #creates text

fuel_bar = canvas.create_text(w-100,80,font = f,fill = 'white')
canvas.after(1000,tick)
root.mainloop()
f_obj.close()

