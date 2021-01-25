from Digits import *
from pyKarel import *

def main():
   wld=World(block=30,width=46,height=10,delay=0.01)
   d1=One(wld,1,9)
   d2 = Five(wld,7,9)
   d3 = Three(wld,13,9)
   d4=One(wld,20,9)
   d5=Nine(wld,27,9)
   d6=Eight(wld,33,9)
   d7=Two(wld,40,9)
   
   d1.display()
   d1.destroy()
   d2.display()
   d2.destroy()
   d3.display()
   d3.destroy()
   d4.display()
   d4.destroy()
   d5.display()
   d5.destroy()
   d6.display()
   d6.destroy()
   d7.display()
   d7.destroy()
   
   wld.mainloop()
   
if __name__ == "__main__":
   main()