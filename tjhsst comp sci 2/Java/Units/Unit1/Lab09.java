//Name: Vivian Feng           Date: March 18,2020

import edu.fcps.karel2.Display;
import edu.fcps.karel2.Robot;
import javax.swing.JOptionPane;

public class Lab09
{
   public static void main(String[] args)
   {
      String filename = JOptionPane.showInputDialog("Which world?");
      Display.openWorld("maps/"+filename+".map");
      Display.setSize(10,10);
      Display.setSpeed(10);
      
      Athlete a = new Athlete(1,1,Display.EAST,Display.INFINITY);
      
      int[] countlist = new int[7];
      for (int i=0;i<7;i++)
      {
         int x = 0;
         while (a.nextToABeeper())
         {
            a.pickBeeper();
            x++;
         }
         countlist[i] = x;
         a.move();
      }
      a.turnAround();
      for (int j=0;j<7;j++)
      {
         a.move();
      }
      a.turnAround();
      a.move();
      
      for (int count:countlist)
      {
         for (int g=0;g<count;g++)
         {
            a.putBeeper();
         }a.move();
      }
   }


}