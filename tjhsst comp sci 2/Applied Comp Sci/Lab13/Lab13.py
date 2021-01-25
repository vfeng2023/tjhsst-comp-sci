#Name: Karthik and Vivian
#Date: 11/11/2019

 ############################################################
#
from Tkinter import Tk,Canvas
from sys import exit
 #
w,h=800,600
#
root=Tk()
cnvs=Canvas(root,width=w,height=h,bg='#D2B48C') # 210 180 140
cnvs.pack()
#
rect1 = cnvs.create_rectangle(0,0,100,100,fill='white',outline='black')
rect2 = cnvs.create_rectangle(0,100,100,200,fill='white',outline='black')
rect3 = cnvs.create_rectangle(0,200,100,300,fill='white',outline='black')
rect4 = cnvs.create_rectangle(0,300,100,400,fill='white',outline='black')
rect5 = cnvs.create_rectangle(0,400,100,500,fill='white',outline='black')
rect6 = cnvs.create_rectangle(0,500,100,600,fill='white',outline='black')

cnvs.create_line(
############################################################
#
def click(evt):
    print 'click',evt.x,evt.y
    
#
def drag(evt):
    print 'drag',evt.x,evt.y
#
def rightclick(evt):
    print 'rightclick',evt.x,evt.y
#
def release(evt):
    print 'release',evt.x,evt.y
#
def one(evt):
    global tool
    #
    tool=1
    print 'tool',tool
#

def quit(evt):
    exit(0)
#
############################################################
#
root.bind('<Button-1>',click)
# root.bind('<
root.mainloop()
