//Name: Vivian Feng and Shriya Muthukumar Date: March 16.2020

import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;

public class Climber extends Athlete
{
   public Climber()
   {
      super();
   }
   public Climber(int x)
   {
      super(x,1,Display.NORTH,1);
   }
   public void climbUpRight()
   {
      //tL,m,m,tR,m
      turnLeft();
      move();
      move();
      turnRight();
      move();
      
   }
   public void climbDownRight(){
      move();
      turnRight();
      move();
      move();
      turnLeft();
     }
     
  public void climbUpLeft(){
   turnRight();
   move();
   move();
   turnLeft();
   move();
  }
  public void climbDownLeft(){
   move();
   turnLeft();
   move();
   move();
   turnRight();
   
  }
   
}