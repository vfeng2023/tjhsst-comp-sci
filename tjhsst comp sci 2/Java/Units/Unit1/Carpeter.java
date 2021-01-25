	//Name______________________________ Date_____________
   import edu.fcps.karel2.Display;
   import edu.fcps.karel2.Robot;
   public class Carpeter extends Robot implements Workable
   {
      public Carpeter(int x, int y)
      {
         super(x, y, Display.EAST, Display.INFINITY);
      }
      public Carpeter()
      {
         super(2, 2, Display.EAST, Display.INFINITY);
      }
      public void workCorner()
      {
         if (nextToABeeper() == false)
         {
            putBeeper();
         }
      }
      public void moveOneBlock()
      {
         move();
      }
      public void turnToTheRight()
      {
         for (int i=1;i<=3;i++)
         {
            turnLeft();
         }
      }
      public void turnToTheNorth()
      {
         while (!facingNorth())
         {
            turnLeft();
         }
      }
   }