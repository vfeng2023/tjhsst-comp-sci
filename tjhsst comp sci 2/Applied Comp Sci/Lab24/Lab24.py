#Name: Vivian Feng and Shriya Muthukumar
# Date: 2.24.2020

#import function from lab 23
from Tkinter import *
import random as rand

from Lab23Func import *

#get dictionary
fontDict = createFontDict()
#instantiate canvas
w = 600
h = 600
root = Tk()
canvas = Canvas(root,width = w, height = h)
canvas.pack()


colors = ['red','orange','yellow','green','blue','indigo','violet']
for state in fontDict.keys():
    fontSize = fontDict[state]
    xcoord = rand.randint(50, w - 50)
    ycoord = rand.randint(50, h - 50)
    print xcoord,ycoord
    canvas.create_text(xcoord, ycoord, text = state,font=('Times New Roman', int(fontSize)), \
                       fill=rand.choice(colors))

def create_states(event):
    global fontDict,canvas
# for each state in dictionary:
    #clear stuff on canvas previously
    # canvas.delete('all')

    #list of colors to choose from
    canvas.delete('all')

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for state in fontDict.keys():
        fontSize = fontDict[state]
        xcoord = rand.randint(50, w - 50)
        ycoord = rand.randint(50, h - 50)
        print xcoord, ycoord
        canvas.create_text(xcoord, ycoord, text=state, font=('Times New Roman', int(fontSize)), \
                           fill=rand.choice(colors))



# - create text based on given font
#  - do so randomly
#
# # bind to space key
root.bind('<space>',create_states)


root.mainloop()
