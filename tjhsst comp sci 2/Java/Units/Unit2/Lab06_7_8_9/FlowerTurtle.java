	//Name______________________________ Date_____________
   import edu.fcps.Turtle;
   import java.awt.Color;
   public class FlowerTurtle extends Turtle
   {
      private double mySize;
      private Color myColor;
      public FlowerTurtle()
      {
         mySize = 50.0;
         myColor = Color.RED;
      }
      public FlowerTurtle(double x, double n, Color c)
      {
         super(x, 300.0, 90.0);
         mySize = n;
         myColor = c;
      }
      public void setSize(double n)
      {
         mySize = n;
      }
      public void setColor(Color c)
      {
         myColor = c;
      }
      private void drawPetals() //starts and ends at center facing north
      {
         super.setColor(myColor);
         for(double theta=0;theta<360;theta+= 360/30){
            forward(mySize);
            turnLeft(180);
            forward(mySize);
            turnRight(180);
            turnLeft(theta);
         }
      
      }
      private void drawStem() //starts at top of stem facing south, ends at bottom
      {
         super.setColor(Color.GREEN);
         forward(mySize * 2.5);
         turnLeft(180);
         forward(mySize * 0.5);
         turnLeft(45);
         forward(mySize*0.5);
         turnLeft(180);
         forward(mySize *0.5);
         turnLeft(90);
         forward(mySize);
         turnLeft(180);
         forward(mySize);
         turnLeft(45);
         forward(mySize * 0.5);
         
      
      }
      public void drawShape()
      {
         drawPetals();
         drawStem();
      }
   }