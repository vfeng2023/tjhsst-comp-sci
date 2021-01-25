import edu.fcps.Turtle;

public class TwistyTurtle2 extends Turtle{

   public TwistyTurtle2(double x,double y,double h){
      super(x,y,h);
   }
   
   public void drawShape(){
      int length = 0;
      int increment = 2;
      double angle = 30;
      
      while(length<150){
         forward(length);
         turnLeft(angle);
         length += increment;
      }

   }
}