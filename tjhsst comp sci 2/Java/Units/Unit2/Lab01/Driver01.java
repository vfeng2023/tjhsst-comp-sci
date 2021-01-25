import javax.swing.JFrame;
public class Driver01{
   
   public static void main(String args[]){
      JFrame frame = new JFrame("Build a House");
      frame.setSize(400,400);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new Panel01());
      frame.setVisible(true);
   
   }

}