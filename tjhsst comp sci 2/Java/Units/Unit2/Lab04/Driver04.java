import javax.swing.*;
import edu.fcps.Bucket;

public class Driver04{

   public static void main(String[] args){
      JFrame frame = new JFrame("Buckets");
      frame.setSize(600,400);
      frame.setLocation(200,200);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new BucketPanel());
      frame.setVisible(true);
      Bucket.setSpeed(1);
      Bucket.useTotal(false); 
      Bucket five = new Bucket(5);
      Bucket three = new Bucket(3);
      five.fill();
      five.pourInto(three);
      three.spill();
      five.fill();
      five.pourInto(three);
   }
}