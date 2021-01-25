public class Driver03{
   public static void main(String args[]){
      int[] array = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109};
      print(array);
      scramble(array);
      print(array);
      sort(array);
      print(array);
   }
   
   //print array
   private static void print(int[] intArray){
      for(int element:intArray){
         System.out.print(element + ",");
      }
      System.out.println();
   }
   //scramble array using Fisher-Yates shuffle
   private static void scramble(int[] banana){
      /*
         from wikipedia:
    -- To shuffle an array a of n elements (indices 0..n-1):
   for i from n−1 downto 1 do
        j ← random integer such that 0 ≤ j ≤ i
        exchange a[j] and a[i]
      */
      for(int i=banana.length-1; i > 0; i--){
         int randomIndex = (int)(Math.random()*i);
         int temp = banana[randomIndex];
         banana[randomIndex] = banana[i];
         banana[i] = temp; 
      }
   }
   //sort array using selection sort
   private static void sort(int[] array){
      for(int n=array.length-1;n >= 0;n--){
         int maxIndex = findMax(array,0,n);
         swap(array,n,maxIndex);
      }
      
   }
   //find maximum value's index of array
   private static int findMax(int[] array,int startIndex,int endIndex){
      int maxPos = 0;
      for(int i=startIndex; i <= endIndex;i++){
         if(array[i] > array[maxPos]) maxPos = i;
      }
      return maxPos;
   }
   //swap to elements in an array
   private static void swap(int[] array, int index1, int index2){
      int temp = array[index1];
      array[index1] = array[index2];
      array[index2] = temp;
   }
   
}