	//Name:      Date: 
import java.io.*;      //the File class
import java.util.*;    //the Scanner class
public class Driver04
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
      Comparable[] array = new Weight[numitems];
      for(int k = 0; k < numitems; k++)
      {
         	int x = infile.nextInt();
            int y = infile.nextInt();
            array[k] = new Weight(x,y);
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
   public static int findMax(Comparable[] array,int endIndex){
      int maxIndex = 0;
      for(int i=0;i<endIndex;i++){
         if( array[i].compareTo(array[maxIndex]) > 0) maxIndex = i;
      }
      return maxIndex;
   }
   public static void swap(Comparable[] array,int index1,int index2){
      Comparable temp = array[index1];
      array[index1] = array[index2];
      array[index2] = temp;
   }
   
   public static void output(Object[] array, String filename) throws Exception
   {
      PrintWriter outFile = new PrintWriter(new FileWriter(filename));
      for(int k = 0; k < array.length; k++)
         outFile.println(array[k].toString());
      outFile.close();
   }
}