#Name:
#Date:

from Politicians import *

def escape(arg):
    arg.walkDownCurrentSegment();    #you know you are not at the end yet
    while not arg.nextToABeeper():
        arg.turnToTheNextSegment()
        arg.walkDownCurrentSegment()

def main():
    world = raw_input("Which 'maze'? ")
    wld=World(world, width=8, height=8, delay=0.1)
    kind = raw_input("What kind of politician? (D, R) ")
    if  kind == "D" or kind == "d":
        candidate = Democrat(wld,1)
    elif kind == "R" or kind == "r":
        candidate = Republican(wld,1)
    else:
        print "Wrong kind"
        sys.exit(0)                 # exists gracefully, if needed
    escape( candidate );
    wld.mainloop()

if __name__=="__main__":
    main()


