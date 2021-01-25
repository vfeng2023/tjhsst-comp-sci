/**
* Game Driver
* @author: Vivian Feng and Shriya Muthukumar, wrote together
* @version: 5.1.2020
*/
import javax.swing.JFrame; //JFrame for game panel
import java.util.*; //scanner class to read file
import java.io.*; //File class

public class GameDriver{

   public static void main(String[] args) throws Exception{
      //generate random states and write to file
      String filename = "cell_states.txt";
      randomizeStates(filename);
      // read random states into array
      Scanner readStates = new Scanner(new File(filename));
      int[] states = new int[400];
         //for loop to read states
      for(int index=0;index<400;index++){
         states[index] = readStates.nextInt();
      } 
      readStates.close();
      // sets up the window
      JFrame frame = new JFrame("Game of Life");
      frame.setSize(400,400);
      frame.setLocation(200,100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new GamePanel(states));
      frame.setVisible(true);
   }

   /**
    * Generates a .txt file containing 400 1s and zeros randomly determined to set the intial states of the game grid.
    * @param filename name of file where states should be written
    * @throws IOException
    */
   public static void randomizeStates(String filename) throws IOException{
      //write states into file with name
      //400 lines long
      PrintWriter pw = new PrintWriter(new FileWriter(filename));
      for(int line=0;line<400;line++){
         pw.println((int)(Math.random()*2));
      }
      pw.close();
      //Sample:
      /*
      1
      0
      1
      1
      ...
      */
   }
}