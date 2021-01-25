from Tkinter import Tk,Canvas

#list with clicks
clicks = []
#master tk frame class
root = Tk()
x = 0
y = 1
#instantiates canvas 
canvas = Canvas(root,width=640,height=480,bg='white')
canvas.pack()
#draws lines
#this method records clicks
def record_click(event):
   global clicks
   clicks.append((event.x,event.y))
   if len(clicks) > 1:
      canvas.create_line(clicks[len(clicks)-2][x],clicks[len(clicks)-2][y],clicks[len(clicks)-1][x],clicks[len(clicks)-1][y])
#reseting clicks
#draws lines between clicks
canvas.bind('<Button-1>',record_click)


root.mainloop()