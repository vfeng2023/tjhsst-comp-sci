//Name: Vivian Feng

import javax.swing.JFrame;

public class Driver03{
   
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Hailstone Numbers");
      frame.setSize(300,200);
      frame.setLocation(200,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new Panel03());
      frame.setVisible(true);
      
   }
}
