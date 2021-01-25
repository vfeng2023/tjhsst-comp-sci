from random import randint
from Lab23Func import createFontDict
from Tkinter import *

w = 1000
h = 800
n = 0
p = randint(0, 5)
randcolour = ["red", "orange", "grey", "green", "blue", "black"]
root = Tk()
canvas = Canvas(root, width = w, height = h, background = "white" )
fontDict = createFontDict()
def space(evt):
    global n,fontDict
    canvas.delete('all')
    states = fontDict.keys()
    n = 0
    while n<50:
        f = ('Times', fontDict[states[n]], 'bold')
        p = randint(0, 5)
        txt = canvas.create_text(randint(100, w-100), randint(100, h-100), text = states[n], \
            font = f, fill = randcolour[p])
        n+=1

root.bind('<space>', space)
space('<space>')
canvas.pack()
root.mainloop()
