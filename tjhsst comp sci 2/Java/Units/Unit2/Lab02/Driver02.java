import javax.swing.*;
public class Driver02{

   public static void main(String[] args){
      JFrame frame = new JFrame("Lab02");
      frame.setSize(300,300);
      frame.setLocation(200,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new Panel02());
      frame.setVisible(true);
      
   }
}