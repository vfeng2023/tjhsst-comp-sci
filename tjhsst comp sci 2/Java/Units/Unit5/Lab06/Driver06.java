//Name: Vivian Feng     Date: UwU

import java.io.File;
import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
public class Driver06{
   public static void main(String args[]) throws Exception{
      //read input.txt into array
      Scanner reader = new Scanner(new File("data.txt"));
      int numLines = reader.nextInt();
      String[] words = new String[numLines];
      for(int j=0;j<numLines;j++){
         words[j] = reader.nextLine();
      }
      reader.close();
      // use selection sort to sort the items
      sort(words);
      
      //write to output
      PrintWriter pw = new PrintWriter(new FileWriter("Output.txt"));
      for(int k=0;k<words.length;k++){
         pw.println(words[k]);
      }
      pw.close();
   }
   
   public static void sort(Comparable[] array){
      for (int ind = array.length-1;ind >= 0; ind--){
         int currMax = findMax(array,ind);
         swap(array,currMax,ind);
      }
   }
   
   public static int findMax(Comparable[] array,int upper){
      int maxPos = 0;
      for(int index=0;index<=upper;index++){
         if (array[index].compareTo(array[maxPos]) > 0) maxPos = index;
      }
      return maxPos;
   }
   public static void swap(Comparable[] array, int a,int b){
      Comparable temp = array[a];
      array[a] = array[b];
      array[b] = temp;
   }
}