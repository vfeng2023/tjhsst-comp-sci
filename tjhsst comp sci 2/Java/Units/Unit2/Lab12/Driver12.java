import javax.swing.*;
import java.awt.*;

public class Driver12{

   public static void main(String args[]){
   
      JFrame frame = new JFrame("Lab 12");
      frame.setSize(400,400);
      frame.setLocation(200,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new PrizePanel());
      frame.setVisible(true);
   }
}