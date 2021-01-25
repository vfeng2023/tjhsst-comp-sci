#Name:
#Date:

from Athlete import *
from random import randint

def main():
    random_width = randint(1,50) + 25
    random_height = randint(1,25) + 12
    random_x = randint(1, random_width)
    random_y = randint(1, random_height)
    wld=World(block = 20, width=random_width, height=random_height)
    wld.addBeeper(random_x, random_y)

    # your code goes here



    wld.mainloop()

if __name__=="__main__":
   main()
