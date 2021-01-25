	//Name______________________________ Date_____________
   import javax.swing.*;
   import java.awt.*;
   import java.awt.event.*;
   public class Panel03 extends JPanel
   {
      private JLabel label1, label2;
      private JTextField box;
      private int number, count;
      public Panel03()
      {
         setLayout(new FlowLayout());
         number = 37;     //number gets 37
         count = 0;
      
         label1 = new JLabel("37");
         label1.setFont(new Font("Serif", Font.BOLD, 100));
         label1.setForeground(Color.blue);
         add(label1);
      
         JPanel panel = new JPanel();
         panel.setLayout(new FlowLayout());
         add(panel);
      
         box = new JTextField("37", 5);
         box.setHorizontalAlignment(SwingConstants.RIGHT);
         panel.add(box);
         
         JButton button1 = new JButton("Set");
         button1.addActionListener(new Listener1());
         panel.add(button1);
      
         JButton button2 = new JButton("Next");
         button2.addActionListener(new Listener2());
         panel.add(button2);
      
         JButton button3 = new JButton("Quit");
         button3.addActionListener(new Listener3());
         panel.add(button3);
      
         label2 = new JLabel("Iterations: 0");
         add(label2);
      }
      private class Listener1 implements ActionListener
      {
         public void actionPerformed(ActionEvent e)
         {  //reset widget
         
            number = Integer.parseInt(box.getText());
            count = 0;
            label1.setText(""+number);
            label2.setText("Iterations: 0");
            
         
         }
      }
      private class Listener2 implements ActionListener
      {
         public void actionPerformed(ActionEvent e)
         {  //find next Hailstone number
            if (number%2 == 0){
               number = number/2;            
            }else{
               number = 3 * number + 1;
            }
            //increment counter
            count++;
            //set labels
            label1.setText(""+number);
            label2.setText("Iteration: "+count);
            
         }
      }
      private class Listener3 implements ActionListener
      {
         public void actionPerformed(ActionEvent e)
         {
            System.exit(0);
         }
      }
   }