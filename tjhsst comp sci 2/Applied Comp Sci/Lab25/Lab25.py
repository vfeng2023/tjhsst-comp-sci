# Name: Vivian Feng and Shriya Muthukumar
# Date: 2.26.2020

# read declaration of independence

import string
import random
from Tkinter import *


# make word lowercase
def lowercase(word):
    return word.lower()


# open declaration of independence
declaration = open('declaration.txt', 'r').read()

# strip punctuation
noPunctDeclaration = declaration.translate(None, string.punctuation)

# add to words to list
wordList = list(map(lowercase, noPunctDeclaration.split()))

# read common words
commonWords = open('common-english-words.txt', 'r').read().split(',')

# remove common words
for word in commonWords:
    while word in wordList:
        wordList.remove(word)

# count frequencies
decWordCount = {}

for phrase in wordList:
    if phrase in decWordCount.keys():
        decWordCount[phrase] += 1

    else:
        decWordCount[phrase] = 1
# find drawn words font size

minFont, maxFont = 12, 50
minCount = min(decWordCount.values())
maxCount = max(decWordCount.values())

drawnWords = {}
for statement in decWordCount.keys():
    if decWordCount[statement] >= 3:
        drawnWords[statement] = int(
            (decWordCount[statement] - minCount) * (maxFont - minFont) / float(maxCount - minCount)
            + minFont)

# draw words onto tkinter canvas

root = Tk()
winWidth = 600
winHeight = 600
canvas = Canvas(root, width=winWidth, height=winHeight)
canvas.pack()
root.title("Lab 24: Wordle of the Declaration of Independence")
def createWordle(event):
    global drawnWords,canvas
    canvas.delete("all")

    # create stuff when clicked
    colors = ['red','orange','grey','green','blue','indigo','violet']
    for word in drawnWords.keys():
        fontSize = drawnWords[word]
        xcoord = random.randint(100, winWidth - 100)
        ycoord = random.randint(100, winWidth - 100)

        canvas.create_text(xcoord, ycoord, text=word, fill=random.choice(colors),
                           font=('Times New Roman', fontSize))

root.bind('<space>',createWordle)
root.mainloop()