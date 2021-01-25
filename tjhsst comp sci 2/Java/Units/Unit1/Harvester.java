//Name: Vivian Feng     Date: March 18,2020

import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;

public class Harvester extends Robot implements Workable
{
   public Harvester()
   {
      super(2,2,Display.EAST,0);
   }
   public Harvester(int x,int y)
   {
      super(x,y,Display.EAST,0);
   }
   
   public void workCorner()
   {
      if (nextToABeeper())
      {
         pickBeeper();
      }
   }
   
   public void moveOneBlock()
   {
      move();
   }
   public void turnToTheRight()
   {
      for (int turn=0;turn<3;turn++)
         turnLeft();
   }
   public void turnToTheNorth()
   {
      while (facingNorth() == false)
      {
         turnLeft();
      }
   }
}
