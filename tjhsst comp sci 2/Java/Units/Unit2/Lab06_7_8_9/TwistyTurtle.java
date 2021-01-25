import edu.fcps.Turtle;
import java.awt.Color;
import javax.swing.*;

public class TwistyTurtle extends Turtle{

   public TwistyTurtle(double x,double y,double h){
      super(x,y,h);
      
   }
   
   public void drawShape(){
      //begin length
      int length = 5;
      //increment
      int increment = 10;
      //angle
      double angle = 123;
      while(length < 400){
         forward(length);
         turnLeft(123);
         length += increment;
      }
      
   }
}