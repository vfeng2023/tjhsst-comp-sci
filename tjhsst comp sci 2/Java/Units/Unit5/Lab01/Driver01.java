	//Name: Vivian Feng    Date:
  

   import java.io.*;
    public class Driver01
   {
       public static void main(String[] args)
      {
      	//input
         double[] myArray = {2.0, 3.7, 9.9, 8.1, 8.5, 7.4, 1.0, 6.2};
      				      
      	//sort the array
         int maxIndex = 0;
         double temp;
      	/*
            for each element of myArray:
               - find largest element in the unsorted array
               - swap
               - move to next element
         */
         for(int index=myArray.length-1;index >= 0;index--){
         
            maxIndex = 0;
            for(int findIndex=0;findIndex < index;findIndex++){
               
               if (myArray[findIndex] > myArray[maxIndex]){
                  maxIndex = findIndex;
               }
            }
            if (myArray[maxIndex] > myArray[index]){
               
               temp = myArray[index];
               myArray[index] = myArray[maxIndex];
               myArray[maxIndex] = temp;
            
            }
         
         
         }		  
      	//output
         for(double element:myArray){
            
            System.out.print(element+" ");
         }
      	
      }
   }