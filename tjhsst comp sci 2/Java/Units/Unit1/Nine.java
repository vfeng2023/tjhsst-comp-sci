import edu.fcps.karel2.Display;
import edu.fcps.Digit;

public class Nine extends Digit 
{
   public Nine(int x,int y)
   {
      super (x,y);
   }
   
   public void display()
   {
      segment1_On();
      segment2_On();
      segment3_On();
      segment4_On();
      segment5_Off();
      segment6_On();
      segment7_On();
      
   }
}