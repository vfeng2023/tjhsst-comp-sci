

	//Name: Vivian Feng Date: 4.17.2020
   import edu.fcps.Turtle;
   import java.awt.Color;
   import javax.swing.*;
    public class Driver06
   {
       public static void main(String[] args)
      {
         JFrame frame = new JFrame("Square Turtles");
         frame.setSize(400, 400);
         frame.setLocation(200, 100);
         frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         frame.setContentPane(new TurtlePanel());
         frame.setVisible(true);
         
         Turtle.setCrawl(true);     //a class method
      
         SquareTurtle smidge = new SquareTurtle();
         smidge.setColor(Color.BLUE);
         smidge.setThickness(6);
         smidge.drawShape();
      
         SquareTurtle joe = new SquareTurtle(60);
         joe.setColor(new Color(0,0,0));
         joe.setThickness(3);
         joe.drawShape();
         
         SquareTurtle bob = new SquareTurtle(200,100,0);
         bob.setColor(Color.RED);
         bob.drawShape();
         
         SquareTurtle stephan = new SquareTurtle(100,100,90,100);
         stephan.setThickness(5);
         stephan.drawShape();
         stephan.setSize(50);
         stephan.drawShape();
      
      }
   }