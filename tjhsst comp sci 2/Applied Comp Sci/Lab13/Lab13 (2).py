#Name: Karthik and Vivian
#Date: 11/11/2019

 ############################################################
#
from Tkinter import Tk,Canvas
from sys import exit
from random import randint
 #
w,h=800,600
#
root=Tk()
cnvs=Canvas(root,width=w,height=h,bg='#D2B48C') # 210 180 140
cnvs.pack()
#defines button rectangles
rect1 = cnvs.create_rectangle(0,0,100,100,fill='white',outline='black')
rect2 = cnvs.create_rectangle(0,100,100,200,fill='white',outline='black')
rect3 = cnvs.create_rectangle(0,200,100,300,fill='white',outline='black')
rect4 = cnvs.create_rectangle(0,300,100,400,fill='white',outline='black')
rect5 = cnvs.create_rectangle(0,400,100,500,fill='white',outline='black')
rect6 = cnvs.create_rectangle(0,500,100,600,fill='white',outline='black')

#define shapes on rectangles
cnvs.create_line(10,10,90,90)
cnvs.create_arc(25,100,75,200,style='arc')
cnvs.create_rectangle(10,210,90,290,fill=None)
cnvs.create_oval(0,400,100,500,fill=None)
for i in range(50):
   pointx = randint(0,100)
   pointy = randint(300,400)
   cnvs.create_oval(pointx-1,pointy-1,pointx+1,pointy+1,fill='black')
black = cnvs.create_rectangle(0,500,50,550,fill='black')
red = cnvs.create_rectangle(50,500,100,550,fill='red')
green = cnvs.create_rectangle(0,550,50,600,fill='green')
blue = cnvs.create_rectangle(50,550,100,600,fill='blue')
############################################################
#necessary conditions
poly_clicks=[]
rect_clicks=[]
oval_clicks = []
color = 'black'
x,y=0,1
#events for each button
#polyline
def draw_line(event):
   global poly_clicks
   if 100<event.x<800:
      poly_clicks.append((event.x,event.y))
      if len(poly_clicks) > 1:
         cnvs.create_line(poly_clicks[-2][x],poly_clicks[-2][y],poly_clicks[-1][x],poly_clicks[-1][y],fill=color)
#draws rectangle      
def draw_rectangle(event):
   global rect_clicks
   if 100<event.x<800:
      rect_clicks.append((event.x,event.y))
      if len(rect_clicks) == 2:
         cnvs.create_rectangle(rect_clicks[0][x],rect_clicks[0][y],rect_clicks[1][x],rect_clicks[1][y],fill=color,outline=color)
         rect_clicks = []
#free draw      
def free_draw(event):
   if 100<event.x<800:
      cnvs.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,fill=color,\
         outline=color)
#spray can      
def spray_can(event):
   if 100<event.x<800:
      for i in range(50):
         pointx = randint(event.x-25,event.x+25)
         pointy = randint(event.y-25,event.y+25)
         if (pointx-event.x)**2 + (pointy-event.y)**2 <= 625:
            cnvs.create_oval(pointx-1,pointy-1,pointx+1,pointy+1,fill=color,outline=color)
#draw oval
def draw_oval(event):     
   global oval_clicks
   if 100<event.x<800:
      oval_clicks.append((event.x,event.y))
      if len(oval_clicks) == 2:
         cnvs.create_oval(oval_clicks[0][x],oval_clicks[0][y],oval_clicks[1][x],oval_clicks[1][y],fill=color,outline=color)
         oval_clicks = []
         
#change color
def change_red(evt):
   global color
   color = 'red'
   
def change_blue(evt):
   global color
   color = 'blue'
   
def change_green(evt):
   global color
   color = 'green'
   
def change_black(evt):
   global color
   color = 'black'


#canvas object bind functions
def bind_line(event):
   global poly_clicks
   cnvs.unbind('<B1-Motion>')
   cnvs.bind("<Button-1>",draw_line)
   poly_clicks = []
   
def bind_rect(event):
   cnvs.bind("<Button-1>",draw_rectangle)
   
def bind_draw(evt):
   cnvs.unbind('<Button-1>')
   cnvs.bind("<B1-Motion>",free_draw)
   
def bind_spray(evt):
   cnvs.bind("<B1-Motion>",spray_can)
   
def bind_oval(evt):
   cnvs.unbind('<B1-Motion>')
   cnvs.bind("<Button-1>",draw_oval)
   
      
############################################################
#
cnvs.tag_bind(rect1,'<Button-1>',bind_line)
cnvs.tag_bind(rect2,'<Button-1>',bind_draw)
cnvs.tag_bind(rect3,'<Button-1>',bind_rect)
cnvs.tag_bind(rect4,'<Button-1>',bind_spray)
cnvs.tag_bind(rect5,'<Button-1>',bind_oval)
cnvs.tag_bind(black,'<Button-1>',change_black)
cnvs.tag_bind(red,'<Button-1>',change_red)
cnvs.tag_bind(blue,'<Button-1>',change_blue)
cnvs.tag_bind(green,'<Button-1>',change_green)

root.mainloop()
