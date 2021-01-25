import javax.swing.*;
import java.awt.*;
public class Panel02 extends JPanel{

   public void paintComponent(Graphics g){
      //draw background and frame
      g.setColor(Color.RED);
      g.fillRect(0,0,500,500);
      g.setColor(new Color(235, 219, 52));
      g.fillRect(25,25,175,225);
      //create ovals around frame 
      int radius = 35/2;
      for(int x=25;x<200;x+=2*radius){
         g.fillOval(x-radius,25-radius,2*radius,2*radius);
         g.fillOval(x-radius,250-radius,2*radius,2*radius);
      }
      //create vertical border
      for(int y=25;y<250;y+=2*radius){
         g.fillOval(25-radius,y-radius,2*radius,2*radius);
         g.fillOval(200-radius,y-radius,2*radius,2*radius);
      
      }
      
      Font font = new Font("Times New Roman",Font.ITALIC,20);
      g.setFont(font);
      g.drawString("Our FearLess Leader",25,300);
      
      ImageIcon thomas = new ImageIcon("tj.jpg");
      g.drawImage(thomas.getImage(),50,50,null);
      
   }
}