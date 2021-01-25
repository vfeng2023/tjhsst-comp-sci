import java.util.*; //the File Class
import java.io.*;// the Scanner Class

public class Driver00{
   public static void main(String args[]) throws Exception{
      Scanner infile = new Scanner(new File("data.txt"));
      int numitems = infile.nextInt();
      double[] array = new double[numitems];
      for(int k=0;k < numitems;k++){
         array[k] = infile.nextDouble();
      }
      infile.close();
      int minPos,maxPos;
      minPos = findMin(array);
      maxPos = findMax(array);
      System.out.println("Minimum Value: "+array[minPos]);
      System.out.println("Maximum value: "+ array[maxPos]);
      
   }
   /**
   * finds the smallest value's index value
   * @param apple array to look through
   * @return index of smallest value in array
   */
   private static int findMin(double[] apple){
     int minIndex = 0;
     for(int i=0;i<apple.length;i++){
         if(apple[i] < apple[minIndex]) minIndex = i;
     } 
     return minIndex;
   }
   /**
   * finds the largest value's index
   * @param array to look through
   * @return index of array's largest value
   */
   private static int findMax(double[] banana){
     int maxIndex = 0;
     for(int index=0; index<banana.length;index++){
         if(banana[index] > banana[maxIndex]){
            maxIndex = index;
         }
     }
     return maxIndex;
   }
}