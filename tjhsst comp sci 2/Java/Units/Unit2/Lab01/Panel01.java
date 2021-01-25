import javax.swing.*;
import java.awt.*;

public class Panel01 extends JPanel{

   public void paintComponent(Graphics g){
      g.setColor(Color.RED);
      g.drawRect(100,200,150,150);
      g.setColor(Color.BLACK);
      g.fillRect(150,275,50,75);
      g.drawLine(0,350,450,350);
      int triX[] = {75,175,275};
      int triY[] = {200,150,200};
      g.drawPolygon(triX,triY,3);
      g.setColor(Color.YELLOW);
      g.fillOval(350,75,50,50);
      g.setColor(Color.WHITE);
      g.setFont(new Font("Serif",Font.BOLD|Font.ITALIC,35));
      g.drawString("Welcome Home",40,40);
      
   }
}