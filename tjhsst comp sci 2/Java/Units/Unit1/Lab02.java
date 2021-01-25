//Name: Vivian Feng and Shriya Muthukumar Date: 3.11.2020

import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;

public class Lab02
{
public static void main(String[] args)
{
   //Open display
   Display.openWorld("maps/maze.map");
   Display.setSize(10,10);
   
   //instantiate default athlete
   Athlete r = new Athlete();
   r.putBeeper();
   r.move();
   r.turnRight();
   r.putBeeper();
   r.move();
   r.turnRight();
   r.putBeeper();
   r.move();
   r.turnLeft();
   r.putBeeper();
   r.move();
   r.turnLeft();
   r.putBeeper();
   r.move();
   r.turnRight();
   r.putBeeper();
   r.move();
   r.putBeeper();
   r.move();
   r.turnRight();
   r.putBeeper();
   r.move();
   r.turnLeft();
   r.putBeeper();
   r.move();
   r.turnLeft();
   r.putBeeper();
   r.move();
   r.putBeeper();
   r.move();
   r.putBeeper();
   r.move();
   r.putBeeper();
   r.move();
   r.turnRight();
   r.putBeeper();
   r.move();
   r.putBeeper();
   r.move();
   
   
}
}