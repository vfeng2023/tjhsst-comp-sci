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
   if len(clicks) == 2:
      canvas.create_line(clicks[0][x],clicks[0][y],clicks[1][x],clicks[1][y])
      clicks = []
#reseting clicks
#draws lines between clicks
canvas.bind('<Button-1>',record_click)





print(clicks)
root.mainloop()