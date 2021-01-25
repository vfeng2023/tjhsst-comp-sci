//Name: Vivian Feng and Shriya Muthukumar Date: 3.13.2020
import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;

public class Lab04
{  //lets athlete take the field
   public static void takeTheField(Athlete arg)
   {
      arg.move();
      arg.move();
      arg.move();
      arg.move();
      arg.turnRight();
      arg.move();
      arg.move();
   }
   public static void main(String[] args)
   {
      //open world
      Display.openWorld("maps/arena.map");
      Display.setSize(10,10);
      Display.setSpeed(10);
      
      //instantiate athletes
      Athlete coach = new Athlete( 2,7, Display.EAST,Display.INFINITY);
      
      Athlete bob = new Athlete();
      Athlete bob1 = new Athlete();
      Athlete bob2 = new Athlete();
      Athlete bob3 = new Athlete();
      Athlete bob4 = new Athlete();
      Athlete bob5 = new Athlete();
         
      //move athletes
      takeTheField(bob);
      takeTheField(bob1);
      takeTheField(bob2);
      takeTheField(bob3);
      takeTheField(bob4);
      takeTheField(bob5);
      
      //Make each athlete assume position
      bob.move();
         bob.move();
         bob.move();
         bob.turnLeft();
         bob.move();
         bob.move();
         bob.turnAround();
         
         bob1.move();
         bob1.turnLeft();
         bob1.move();
         bob1.turnAround();
         
         bob2.move();
         bob2.move();
         bob2.turnRight();
         
         bob3.move();
         bob3.move();
         bob3.move();
         bob3.turnRight();
         
         bob4.move();
         bob4.move();
         bob4.move();
         bob4.move();
         bob4.turnRight();
         
         bob5.move();
         bob5.move();
         bob5.move();
         bob5.move();
         bob5.move();
         bob5.turnLeft();
         bob5.move();
         bob5.turnAround();  
   }
}