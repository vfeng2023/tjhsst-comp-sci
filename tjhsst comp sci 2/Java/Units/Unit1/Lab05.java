//Name: Vivian Feng     Date: March 17,2020

import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;

public class Lab05
{
   public static void runTheRace(Racer arg)
   {
      int[] beeperList = {7,5,3};
      
      /*for each pile:
         - go to pile and go back*/
      int spaces = 2;
      for (int pile=0;pile<3;pile++)
      {
         arg.shuttle(spaces,beeperList[pile]);
         spaces += 2;
      }
      arg.move();
   }
   
   public static void main(String[] args)
   {
      Display.openWorld("maps/shuttle.map");
      Display.setSize(10,10);
      Display.setSpeed(10);
      
      Racer bob = new Racer(1);
      Racer joe = new Racer(4);
      Racer rick = new Racer(7);
      
      runTheRace(bob);
      runTheRace(joe);
      runTheRace(rick);
   }
}