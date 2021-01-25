    //Torbert, e-mail: smtorbert@fcps.edu	
	 //version 6.17.2003
	 //version 11.4.09  mlbillington@fcps.edu
   import javax.swing.*;
   import java.awt.*;
   import java.awt.event.*;
   import java.awt.image.*;
    public class BugPanel extends JPanel
   {
      private BufferedImage myImage;
      final int N = 400;
       public BugPanel()
      {
         myImage = new BufferedImage(N, N, BufferedImage.TYPE_INT_RGB);
         Graphics buffer = myImage.getGraphics();
         buffer.setColor(Color.BLUE);
         buffer.fillRect(0, 0, N, N);
         buffer.setColor(Color.YELLOW);
         /*
         1.	 Instantiate 4 bugs, one at each corner.
         2.	 Tell each bug to move 10% of the way toward its clockwise neighbor.
         3.	 Draw a line between each bug.
         4.	 Repeat steps 2 and 3 until any two bugs are at the same spot.
         */
         
         //create bugs
         Bug b1 = new Bug(0,0);
         Bug b2 = new Bug(N,0);
         Bug b3 = new Bug(N,N);
         Bug b4 = new Bug(0,N);
         Bug oldb1 = new Bug(0,0);
         while(!(b1.sameSpot(b2)|b2.sameSpot(b3)|b3.sameSpot(b4)|b4.sameSpot(b1))){
            b1.walkTowards(b2,0.9);
            b2.walkTowards(b3,0.9);
            b3.walkTowards(b4,0.9);
            b4.walkTowards(oldb1,0.9);
            oldb1.walkTowards(b1,1);
            buffer.drawLine(b1.getX(),b1.getY(),b2.getX(),b2.getY());
            buffer.drawLine(b2.getX(),b2.getY(),b3.getX(),b3.getY());
            buffer.drawLine(b3.getX(),b3.getY(),b4.getX(),b4.getY());
            buffer.drawLine(b4.getX(),b4.getY(),b1.getX(),b1.getY());
            
         }
         
         
      
      }
       public void paintComponent(Graphics g)
      {
         g.drawImage(myImage, 0, 0, getWidth(), getHeight(), null);
      }
   }