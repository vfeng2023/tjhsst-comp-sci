//Name: Vivian Feng and Shriya Muthukumar Date: March 16,2020

import edu.fcps.karel2.Display;
import edu.fcps.karel2.Robot;

public class Lab03
{
   public static void main(String[] args){
      Display.openWorld("maps/mountain.map");
      Display.setSize(16,16);
      Climber t = new Climber(8);
      Climber r= new Climber(8);
      
      r.putBeeper();
      r.turnRight();
      t.turnRight();
      r.move();
      t.move();
      r.climbUpRight();
      t.climbUpRight();
      r.climbUpRight();
      t.climbUpRight();
      r.climbUpRight();
      t.climbUpRight();
      
      t.climbDownRight();
      r.climbDownRight();
      t.climbDownRight();
      r.climbDownRight();
      
      r.pickBeeper();
      r.turnAround();
      t.turnAround();
      t.climbUpLeft();
      r.climbUpLeft();
      t.climbUpLeft();
      r.climbUpLeft();
      t.climbDownLeft();
      r.climbDownLeft();
      t.climbDownLeft();
      r.climbDownLeft();
      t.climbDownLeft();
      r.climbDownLeft();
      t.move();
      r.move();
      t.putBeeper();
      r.move();
      t.move();
   }
}