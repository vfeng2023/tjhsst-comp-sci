   //Name:    Date:   import javax.swing.*;
   import java.awt.*;
   import java.awt.event.*;
   import java.awt.image.*;
   import javax.swing.*;
    public class PrizePanel extends JPanel
   {
      private static final int FRAME = 400;
      private static final Color BACKGROUND = new Color(204, 204, 204);
      private BufferedImage myImage;
      private Graphics myBuffer;
      private Ball ball;
      private Polkadot pd;
      private Timer t;
      private int hits;
      private JButton button; 
		//constructor   
       public PrizePanel()
      {  
         setLayout(new FlowLayout());
         myImage = new BufferedImage(FRAME,FRAME,BufferedImage.TYPE_INT_RGB);
         myBuffer = myImage.getGraphics();
         myBuffer.setColor(BACKGROUND);
         myBuffer.fillRect(0,0,FRAME,FRAME);
         int ballX = (int)(Math.random()*(FRAME-100)+50);
         int ballY = (int)(Math.random()*(FRAME-100)+50);
         int pdX = (int)(Math.random()*(FRAME-50)+25);
         int pdY = (int)(Math.random()*(FRAME-50)+25);
         
        button = new JButton("Start");
         button.addActionListener(new ButtonListener());
         add(button);
         
         pd = new Polkadot(pdX,pdY,50,Color.RED);
         ball = new Ball(ballX,ballY,100,Color.BLACK); 
         
         
         
         
      }
       public void paintComponent(Graphics g)
      {
         g.drawImage(myImage,0,0,getWidth(),getHeight(),null);
      }
      
      private class ButtonListener implements ActionListener{
         public void actionPerformed(ActionEvent e){
            button.setEnabled(false);
            t = new Timer(5,new Listener());
            t.start();
            
         }
      }
       private class Listener implements ActionListener
      {
          public void actionPerformed(ActionEvent e)
         {
            myBuffer.setColor(BACKGROUND);
            myBuffer.fillRect(0,0,FRAME,FRAME);
            ball.move(FRAME,FRAME);
            collide(ball,pd);
            
            ball.draw(myBuffer);
            pd.draw(myBuffer);
            
            myBuffer.setColor(Color.BLACK);
            myBuffer.setFont(new Font("Monospaced",Font.BOLD,24));
            myBuffer.drawString("Count: "+hits,FRAME-150,25);
            
            repaint();
            
         }
      }   
       private void collide(Ball b, Polkadot pd)
      {
        double d = distance(b.getX(),b.getY(),pd.getX(),pd.getY());
        if ( d <=  b.getRadius() + pd.getRadius()){
            hits++;
            pd.setX((int)(Math.random()*(FRAME-50)+25));
            pd.setY((int)(Math.random()*(FRAME-50)+25));
        }
		
		  
      }
       private double distance(double x1, double y1, double x2, double y2)
      {
         return Math.sqrt(Math.pow(x2-x1,2)+Math.pow(y2-y1,2));
      }
   }