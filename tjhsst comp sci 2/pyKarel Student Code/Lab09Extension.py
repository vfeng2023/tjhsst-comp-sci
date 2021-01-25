# Name:
# Date:

from pyKarel import *
from Shifter import *

def main():
    name_of_world=raw_input("Which 'pile'? ")
    wld=World(name_of_world, width=8, height=3, delay=0.1)
    r = Shifter(wld, 1,1, east)
    r.shift_piles()
    wld.mainloop()
    
if __name__=="__main__":
    main()          
       
    

