from pyKarel import *
from Swimmer import *
from threading import Thread

def myfunc(arg):
   arg.swim_laps()
   
def main():
   wld=World()
   weismuller = Swimmer(wld,2)
   fraser = Swimmer(wld,4)
   spitz = Swimmer(wld,6)
   phelps = Swimmer(wld,8)
   t1=Thread(target=myfunc,args=(weismuller,))
   t2=Thread(target=myfunc,args=(fraser,))
   t3=Thread(target=myfunc,args=(spitz,))
   t4=Thread(target=myfunc,args=(phelps,))
   
   t1.start()
   t2.start()
   t3.start()
   t4.start()
   
   wld.mainloop()
   
if __name__=="__main__":
   main()