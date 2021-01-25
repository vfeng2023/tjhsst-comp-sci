//Name: Vivian Feng        Date: March 18,2020

import edu.fcps.karel2.Display;
import edu.fcps.karel2.Robot;

public class SteepleChaseRacer extends Racer
{
   public SteepleChaseRacer(int y)
   {
      super(y);  
   }
   public void jumpRight();
   {
      turnLeft();
      while (rightIsClear() == false)
         move();
      turnRight();
      move();
      turnRight();
      
      while (frontIsClear())
         move();
         
      turnLeft();
   }
}