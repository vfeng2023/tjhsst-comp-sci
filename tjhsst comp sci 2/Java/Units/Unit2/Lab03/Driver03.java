import javax.swing.*;
public class Driver03{

   public static void main(String[] args){
      
      JFrame frame = new JFrame("Lab03");
      frame.setSize(400,400);
      frame.setLocation(200,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new Panel03());
      frame.setVisible(true);
   }
}