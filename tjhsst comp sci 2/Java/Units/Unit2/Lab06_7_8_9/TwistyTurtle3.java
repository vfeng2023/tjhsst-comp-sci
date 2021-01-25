import edu.fcps.Turtle;

public class TwistyTurtle3 extends Turtle{

   public TwistyTurtle3(double x,double y,double h){
      
      super(x,y,h);
   }
   
   public void drawShape(){
      int length = 25;
      int increment = 5;
      int angle = 45;
      
      while(length<150){
         for(int i=0;i<4;i++){
            forward(length);
            turnLeft(90);
         }
         turnLeft(angle);
         length += increment;
      }
      
   }
}