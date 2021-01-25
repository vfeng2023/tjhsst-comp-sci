/*
   Triangle is and equilateral triangle
*/
public class Triangle extends Shape{
   
   private double mySide;
   
   public Triangle(double x){
      mySide = x;
   }
   
   public double findArea(){
      return Math.sqrt(3)/4*mySide*mySide;
   }
   
   public double findPerimeter(){
      
      return 3*mySide;
   }
   
   public double getSide(){
      return mySide;
   }
   public void setSide(double x){
      mySide = x;
   }
   

}