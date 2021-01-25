import javax.swing.*;
import java.awt.Color;
public class Driver11{

   public static void main(String[] args){
      
      JFrame frame = new JFrame("Pinball");
      frame.setSize(400,400);
      frame.setLocation(200,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new PinballPanel());
      frame.setVisible(true);
      
   }
}