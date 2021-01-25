#Name:
#Date:

from pyKarel import *

def main():       
     name_of_world=raw_input("Which 'tasks' world? ")
     global wld
     wld=World(name_of_world, delay=0.1)
     if name_of_world == 'tasks7_12_1' or 'tasks7_12_2':
          task_07()
          task_08()
          task_09()
          task_10()
          task_11()
          task_12()
     else:
          task_01()  #go to the end of the row of beepers
          task_02()  #go to the beeper
          task_03()  #go to the wall
          task_04()  #go to the wall, pick up all the beepers (max one per pile)
          task_05()  #go to the wall, pick up all the beepers
          task_06() #go to the end of the row of beepers, there is one gap
    
     wld.mainloop()

def task_01():	  #go to the end of the row of beepers
     temp = Robot(wld, 1, 1, east, 0) 
     while temp.nextToABeeper():
          temp.move()
     

def task_02():    #go to the beeper
     temp = Robot(wld, 1, 2, east, 0) 
     while not temp.nextToABeeper():
          temp.move()
     
       
def task_03():	  #go to the wall
     temp = Robot(wld, 1, 3, east, 0) 
     while temp.frontIsClear() == True:
          temp.move()
          
def task_04():	  #go to the wall, pick up all the beepers (max one per pile)
     temp = Robot(wld, 1, 4, east, 0)
     while temp.frontIsClear():
          if temp.nextToABeeper():
               temp.pickBeeper()
          temp.move()
          
def task_05():	  #go to the wall, pick up all the beepers
     temp = Robot(wld, 1, 5, east, 0)
     while temp.frontIsClear():
          while temp.nextToABeeper():
               temp.pickBeeper()
          temp.move()
     while temp.nextToABeeper():
          temp.pickBeeper()
def task_06():    #go to the end of the row of beepers, there is one gap
     temp = Robot(wld, 1, 6, east, 0) 
     while temp.nextToABeeper():
          temp.move()
     temp.move()
     while temp.nextToABeeper():
          temp.move()
def task_07():
     temp = Robot(wld,1,1,east,0)
     x = 0
     while (temp.nextToABeeper() or temp.frontIsClear) == True:
           temp.move()
           x+=1
     print "The count is ",x

def task_08():
     temp = Robot(wld,1,2,beepers = 9)
     labor = Robot(wld,6,2)
     while not temp.nextToARobot():
          temp.move()
def task_09():
     temp = Robot(wld,1,3,beepers = 20)
     for i in range(5):
          for j in range(4):
               temp.putBeeper()
          temp.move()

def task_10():
     temp = Robot(wld,1,4,beepers = infinity)
     while temp.frontIsClear():
          temp.move()
          if not temp.nextToABeeper():
               temp.putBeeper()
def task_11():
     temp = Robot(wld,1,5,beepers = infinity)
     while not temp.rightIsClear():
          temp.putBeeper()
          temp.move()
def task_12():
     temp = Robot(wld,1,6)
     while not(temp.nextToABeeper() and temp.rightIsClear()):
          temp.move()
if __name__=="__main__":
     main()
   
