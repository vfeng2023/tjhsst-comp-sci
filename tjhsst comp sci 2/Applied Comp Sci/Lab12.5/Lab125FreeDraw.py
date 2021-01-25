#Name: Vivian Feng and Karthik Bhurgav
#Date: 11/6/2019

from Tkinter import Tk,Canvas
#instantiate canvas and tk master object

root = Tk()
canvas = Canvas(root,height = 480,width=640)
canvas.pack()
#defines first click
first_click = True
x = None
y = None
#detect click
def click(event):
   global first_click
   first_click = True
   
#create line while dragging mouse through lots of points
def drag(event):
   global first_click
   if first_click == True:
      canvas.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,fill='blue',\
      outline='blue')
   
#detect release of mouse
def release(event):
   global first_click
   first_click = False
#clears canvas
def clear(event):
   canvas.delete('all')
#stop when mouse is released
canvas.bind('<Button-1>',click)
canvas.bind('<B1-Motion>',drag)
canvas.bind('<ButtonRelease-1>',release)
root.bind('<c>',clear)
root.mainloop()