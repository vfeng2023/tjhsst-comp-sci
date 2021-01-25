	//Name:   Date:
import java.io.*;      //the File class
import java.util.*;    //the Scanner class
public class Driver02
{
   public static void main(String[] args) throws Exception
   {
      double[] array = input("data.txt");
      sort(array);
      output(array, "output.txt");
   }
   public static double[] input(String filename) throws Exception
   {
       Scanner sc = new Scanner(new File(filename));
       int size = sc.nextInt();
       double[] nums = new double[size];
       for(int k=0;k<nums.length;k++){
         nums[k] = sc.nextDouble();
       }
       sc.close();
       return nums;
   }
   public static void sort(double[] array)
   {
      int maxPos;
      for(int k = 0; k < array.length; k++)
      {
         maxPos = findMax(array, array.length - k - 1);
         swap(array, maxPos, array.length - k - 1);
      }
   }
   public static int findMax(double[] array, int upper) //what does "upper" do???
   {
      int maxIndex = 0;
      for(int k=0;k<=upper;k++){
         if(array[k] > array[maxIndex]) maxIndex = k;
      }
      return maxIndex;
   }
   public static void swap(double[] array, int a, int b)//what are "a" and "b" for???
   {
        double temp = array[a];
        array[a] = array[b];
        array[b] = temp;
   }
   public static void output(double[] array, String filename) throws Exception
   {
        PrintWriter pw = new PrintWriter(new FileWriter(filename));
        for(int i=0;i<array.length;i++){
            pw.println(array[i]);
        }
   }
}