 //name:    date:  

import java.io.*;      //the File class
import java.util.*;    //the Scanner class
import javax.swing.JOptionPane;
public class Driver04
{
      //find sum
   public static double findSum(double[] array){
      double sum;
      sum = 0;
      for(int index = 0;index<array.length;index++){
         sum = sum+array[index];
      }
      return sum;
   }
      //find average
      
   public static double findAvg(double[] array){
      double total;
      total = findSum(array);
      double avg;
      avg = total/array.length;
      
      return avg;
   }
      
      //find min
      
   public static double findMin(double[] array){
      double min=array[0];
      for (int index=0;index<array.length;index++)
      {
         if (array[index]<min)
            min = array[index];
      }
      return min;
   }
      
      //find max
      
   public static double findMax(double[] array){
      double max = array[0];
      for(int index=0;index<array.length;index++)
      {
         if(array[index]>max)
            max = array[index];
      }
      return max;
   }
   public static void main(String[] args) 
   {
      Scanner infile = null;
      try
      {
         String filename = JOptionPane.showInputDialog("Enter file name: ");
         infile = new Scanner( new File(filename));
      }catch(FileNotFoundException e)
      {
         JOptionPane.showMessageDialog(null,"Error: File not Found");
         System.exit(0);
      }
      int ARRAYSIZE = infile.nextInt();
      double[] nums = new double[ARRAYSIZE];
      
      for(int index=0;index<nums.length;index++){
         nums[index] = infile.nextDouble();
      }
      
      double sum,avg,min,max;
      
      sum = findSum(nums);
      avg = findAvg(nums);
      min = findMin(nums);
      max = findMax(nums);
      
      System.out.println("Sum: "+sum);
      System.out.println("Avg: "+avg);
      System.out.println("Min: "+min);
      System.out.println("Max: "+max);
   }
}
/************************************
Sum: 3291074.1965423366
Avg: 504.3791872095535
Min: 0.027375512843708094
Max: 999.9780398236477

*************************************/