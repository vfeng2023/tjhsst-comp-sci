// Name: Vivian Feng             March 17,2020

import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;
import javax.swing.JOptionPane;

public class Lab10
{
   public static void followWallsRight(Athlete arg)
   {
      while (arg.nextToABeeper() == false)
      {  //decide what to do if front has wall
         if (arg.frontIsClear() == false){
            int clear = 0;
            //checks left and right for walls
            if (arg.leftIsClear()){
               clear ++;
            }
            if ( arg.rightIsClear())
            {
               clear ++;
            }
            //turns right is possible. otherwise, turn left
            if (clear==2)
               arg.turnRight();
            
            else if (clear==1)
            {
               if (arg.rightIsClear())
                  arg.turnRight();
                  
               else
                  arg.turnLeft();
                  
            }else{
               arg.turnAround();
            }
         }else{
            if (arg.rightIsClear())
               arg.turnRight();
               
         }
         arg.move();
      }
   }
   
   public static void main(String[] args){
      String filename = JOptionPane.showInputDialog("Which maze(maze1,maze2,maze3)? ");
      Display.openWorld("maps/"+filename+".map");
      Display.setSize(10,10);
      Display.setSpeed(5);
      Athlete karel = new Athlete();
      followWallsRight(karel);
   }
}