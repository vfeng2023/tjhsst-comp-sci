//Torbert, e-mail: mr@torbert.com, website: www.mr.torbert.com
//version 7.14.2003

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Panel09 extends JPanel
{
   ScoreCard09 scorecard = new ScoreCard09();
   JLabel output;
   public Panel09()
   {
      setLayout(new BorderLayout());
   
      output = new JLabel("------", SwingConstants.CENTER);
      add(output, BorderLayout.NORTH);
   
      add(scorecard, BorderLayout.CENTER);
   
      JPanel subpanel = new JPanel();
      subpanel.setLayout(new FlowLayout());
      /*  add the buttons to the subpanel  */
      addButton(subpanel,"Randomize",new Listener1());
      addButton(subpanel,"Hardest Hole",new Listener2());
      addButton(subpanel,"Total Score",new Listener3());
      addButton(subpanel,"Holes in One",new Listener4());
      
      add(subpanel, BorderLayout.SOUTH);
      
   }
   private void addButton(JPanel p, String s, ActionListener a)
   {
      JButton b = new JButton(s);
      b.addActionListener(a);
      p.add(b);
   }
   private class Listener1 implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         scorecard.randomize();
         output.setText("------");
      }
   }
   private class Listener2 implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
        int hardestHole = scorecard.findHardestHole();
        output.setText("Hardest hole: "+hardestHole);
      }
   }
   private class Listener3 implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         int totalScore = scorecard.findTotal();
         output.setText("Total score: "+totalScore);
      }
   }
   private class Listener4 implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         int ace = scorecard.findAces();
         output.setText("Holes in One: "+ace);
      }
   }
}