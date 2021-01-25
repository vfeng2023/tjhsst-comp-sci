/*
   Square is a child class of Rectangle, because squares are a special case of rectangles
*/

public class Square extends Rectangle{
   
   public Square(double x){
      super(x,x);
   }
   
   public double getSide(){
   
      return getHeight();
   }
   
   public void setSide(double x){
      setHeight(x);
      setBase(x);
   }
}