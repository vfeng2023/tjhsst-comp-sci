#Name:
#Date:

from pyKarel import *

def main():       
     name_of_world=raw_input("Which 'tasks' world? ")
     global wld
     wld=World(name_of_world, delay=0.1)
     task_01()  #go to the end of the row of beepers
     task_02()  #go to the beeper
     task_03()  #go to the wall
     task_04()  #go to the wall, pick up all the beepers (max one per pile)
     task_05()  #go to the wall, pick up all the beepers
     task_06()  #go to the end of the row of beepers, there is one gap
     wld.mainloop()

def task_01():	  #go to the end of the row of beepers
     temp = Robot(wld, 1, 1, east, 0) 
     # write code here
     

def task_02():    #go to the beeper
     temp = Robot(wld, 1, 2, east, 0) 
     # write code here
     
       
def task_03():	  #go to the wall
     temp = Robot(wld, 1, 3, east, 0) 
     # write code here
     
       
def task_04():	  #go to the wall, pick up all the beepers (max one per pile)
     temp = Robot(wld, 1, 4, east, 0) 
     # write code here
     

def task_05():	  #go to the wall, pick up all the beepers
     temp = Robot(wld, 1, 5, east, 0) 
     # write code here
     

def task_06():    #go to the end of the row of beepers, there is one gap
     temp = Robot(wld, 1, 6, east, 0) 
     # write code here

     
            
if __name__=="__main__":
     main()
   
