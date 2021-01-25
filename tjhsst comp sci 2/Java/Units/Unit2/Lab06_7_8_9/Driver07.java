	//Name______________________________ Date_____________
   import edu.fcps.Turtle;
   import java.awt.Color;
   import javax.swing.*;
   public class Driver07
   {
      public static void main(String[] args)
      {
         JFrame frame = new JFrame("Polygon Turtles");
         frame.setSize(400, 400);
         frame.setLocation(200, 100);
         frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         frame.setContentPane(new TurtlePanel());
         frame.setVisible(true);
      
         PolygonTurtle smidge = new PolygonTurtle(100.0, 3);
         smidge.setColor(Color.BLUE);
         smidge.setThickness(6);
         smidge.drawShape();
         
         PolygonTurtle joe = new PolygonTurtle();
         joe.drawShape();
         
         PolygonTurtle bob = new PolygonTurtle(100,100,90,70,3);
         bob.drawShape();
         
         PolygonTurtle[] turtles = new PolygonTurtle[7];
         int sides = 3;
         int x = 10;
         for( int i=0; i<turtles.length;i++){
            
            turtles[i] = new PolygonTurtle(x,200,0,50,sides);
            x+=20;
            sides++;
         }
         
         for(int i=0;i<turtles.length;i++){
            turtles[i].drawShape();
         }
      
         
      
      }
   }