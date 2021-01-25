	//Name:      Date: 
import java.io.*;      //the File class
import java.util.*;    //the Scanner class
public class Driver05
{
   public static void main(String[] args) throws Exception
   {
      Comparable[] apple = input("data.txt");
      sort(apple);
      output(apple, "output.txt");
   }
   	
   public static Comparable[] input(String filename) throws Exception
   {	
      Scanner infile = new Scanner( new File(filename) );
      int numitems = infile.nextInt();
      Comparable[] array = new Distance[numitems];
      for(int k = 0; k < numitems; k++)
      {
        int feet = infile.nextInt();
        int inches = infile.nextInt();
        array[k] = new Distance(feet,inches);
      }
      infile.close();
      return array;
   }
          
   public static void sort(Comparable[] array)
   {
      int maxPos;
      for(int k = 0; k < array.length; k++)
      {
         maxPos = findMax(array, array.length - k);
         swap(array, maxPos, array.length - k - 1);
      }
   }
   
   //find maximum distance object given array of distance objects
   public static int findMax(Comparable[] array,int toLength){
      
      int maxIndex = 0;
      for (int i=0;i < toLength;i++){
         
         if (array[i].compareTo(array[maxIndex]) == 1){
            maxIndex = i;
         }
      }
      return maxIndex;
   }
   public static void swap(Comparable[] array, int pos1, int pos2){
   
      Comparable temp = array[pos1];
      array[pos1] = array[pos2];
      array[pos2] = temp;
   }
   
   public static void output(Object[] array, String filename) throws Exception
   {
      PrintWriter outFile = new PrintWriter(new FileWriter(filename));
      for(int k = 0; k < array.length; k++)
         outFile.println(array[k].toString());
      outFile.close();
   }
}