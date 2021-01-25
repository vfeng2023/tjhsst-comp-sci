//Name: Vivian Feng Date: 4/29/2020
import java.io.*; //get filewriter class
public class Driver07{
   public static final int ARRAYSIZE = (int)(50+Math.random()*51);
   public static void main(String args[]) throws Exception{ 
      //instantiate array
      Shape[] shapeArray = new Shape[ARRAYSIZE];
      //populate array with shapes
      for(int i=0;i<ARRAYSIZE;i++){
         int choice = (int)(1+Math.random()*4);
         if(choice == 1){
            shapeArray[i] = new Circle(10+Math.random()*10);
         }else if(choice == 2){
            shapeArray[i] = new Square(10+Math.random() * 10); 
         }else if(choice == 3){
            shapeArray[i] = new Rectangle(10+Math.random()*10,10+Math.random()*10);
            
         }else{
            shapeArray[i] = new Triangle(10+Math.random()*10);
         }
        
      }
      //write random shapes area to file
      PrintWriter toFile = new PrintWriter(new FileWriter("output.txt"));
      toFile.println("Shapes");
      toFile.println("------");
      for(int index=0;index<shapeArray.length;index++){
         toFile.println("area = "+shapeArray[index].findArea()+"\t\t"+shapeArray[index].toString());
      }       
      toFile.close();
   }
}