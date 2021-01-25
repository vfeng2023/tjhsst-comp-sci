	//Name______________________________ Date_____________
   import edu.fcps.Turtle;
   import java.awt.Color;
   import javax.swing.*;
   public class Driver08
   {
      public static void main(String[] args)
      {
         JFrame canvas = new JFrame("Flowers");
         canvas.setSize(400,400);
         canvas.setLocation(200,100);
         canvas.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         canvas.setContentPane(new TurtlePanel());
         canvas.setVisible(true);
         Turtle.setCrawl(false);
         Turtle.clear(new Color(255,255,255));
         FlowerTurtle smidge = new FlowerTurtle();
         smidge.drawShape();  
         
         FlowerTurtle joe = new FlowerTurtle(50,100,new Color(35,45,67));
         FlowerTurtle bob = new FlowerTurtle(100,75,new Color(0,0,255));
         FlowerTurtle jim = new FlowerTurtle(150,75,new Color(255,24,56));
         
         joe.drawShape();
         bob.drawShape();
         jim.drawShape();
      }
   }