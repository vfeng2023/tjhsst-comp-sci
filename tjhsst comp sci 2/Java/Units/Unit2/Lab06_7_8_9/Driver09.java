import edu.fcps.Turtle;
import java.awt.Color;
import javax.swing.*;

public class Driver09{

   public static void twisties(Turtle arg){
	arg.setPenDown(false);
   arg.turnRight((int)(Math.random() * 360));
	arg.forward((int)(Math.random() * 200));
	arg.setPenDown(true);
   arg.drawShape(); 
   }


   public static void main(String[] args){
      
      JFrame frame = new JFrame("Twisty Turtles");
      frame.setSize(400,400);
      frame.setLocation(200,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new TurtlePanel());
      frame.setVisible(true);
      
      Turtle.setCrawl(false);
      Turtle.clear(new Color(160,160,160));
      
      
      TwistyTurtle smidge = new TwistyTurtle(200,200,0);
      twisties(smidge);
      
      TwistyTurtle2 joe = new TwistyTurtle2(200,200,0);
      joe.setColor(Color.BLUE);
      twisties(joe);
      
      TwistyTurtle3 bob = new TwistyTurtle3(200,200,0);
      bob.setColor(Color.GREEN);
      twisties(bob);
   }
}