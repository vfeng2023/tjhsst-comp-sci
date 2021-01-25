import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Panel00 extends JPanel{
   private JLabel label;   //reference in a field
   public Panel00()
   {
      setLayout(new FlowLayout());

      label = new JLabel("0.00000000000000");
      label.setFont(new Font("Serif",Font.BOLD,20));
      label.setForeground(Color.blue);
      add(label);

      JButton button = new JButton("Random"); //local
      button.addActionListener(new Listener());
      add(button);
      
      addMouseListener(new ClickListener());
   }
   private class Listener implements ActionListener{
      public void actionPerformed(ActionEvent e){
         label.setText(""+Math.random());
      }
   }
   private class ClickListener extends MouseAdapter{
      public void mouseClicked(MouseEvent e){
         System.out.println("You clicked at ("+e.getX()+","+e.getY()+")");
      }
   } 
}