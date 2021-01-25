	//Name______________________________ Date_____________
   import javax.swing.*;
   import java.awt.*;
   public class ScoreCard09 extends JPanel
   {
      private JTextField[] input;
      public ScoreCard09()
      {
         setLayout(new GridLayout(2, 18));
         /* add 18 JLabels  */
         JLabel[] labels = new JLabel[18];
         for( int z=0;z<labels.length;z++){
         
            labels[z] = new JLabel(""+(z+1));
            add(labels[z]);
         }
         
   
   
         /* add an array of 18 JTextFields  */
         input = new JTextField[18];
         for(int x = 0;x<input.length;x++){
         
            input[x] = new JTextField();
            add(input[x]);
            
         }
      }
      public void randomize()
      {  
         int randNum;
         for (int i=0;i<input.length;i++){
            randNum = (int)(Math.random()*4+1);
            input[i].setText(""+randNum);
       }
      }
      public int findTotal()
      {  
         //get scores
         int score;
         int[] scores = new int[input.length];
         for(int i=0;i<scores.length;i++){
            score = Integer.parseInt(input[i].getText());
            scores[i] = score;
         }
         //find total
         int total=0;
         for(int scoreIndex=0;scoreIndex<scores.length;scoreIndex++){
            
            total = total + scores[scoreIndex];
         }
         return total;
         
      }
      public int findAces()
      {
         int numAces = 0;
         for(int hole=0;hole<input.length;hole++){
            int score = Integer.parseInt(input[hole].getText());
            if (score == 1)
               numAces++;
         }
         return numAces;
      }
      public int findHardestHole()
      {
         int val;
         int max = Integer.parseInt(input[0].getText());;
         //iterate through list to find largest value
         for(int g=0;g<input.length;g++){
            
            val = Integer.parseInt(input[g].getText());
            if (val > max)
               max = val;
      
         }
         //iterate through list again to see which values have max, returning 1st match
         
         int hardest=0,holeVal;
         for(int holeInd = 0;holeInd < input.length;holeInd++){
            
            holeVal = Integer.parseInt(input[holeInd].getText());
            if (holeVal == max){
               hardest = holeInd+1;
               break;
            }
         }
         return hardest;
      }
   }