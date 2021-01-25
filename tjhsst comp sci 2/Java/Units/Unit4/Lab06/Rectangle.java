/************************************************************
* A rectangle is a shape that mantains information about its height and width. 
* A rectangle knows how to set its base and height, return its base and height, 
* find its area, calculate its area, and find the length of its diagonal
* @author Vivian Feng
* @version 4.28.2020
***********************************************************************/

public class Rectangle extends Shape{

   
   private double myBase,myHeight;
   /*************************************************************************
   * Construct a rectangle with initial height and with specified by x and y
   * @param x initial base
   * @param y initial height
   **************************************************************************/
   public Rectangle(double x,double y){
      
      myBase = x;
      myHeight = y;
      
   }
   /***********************************************************
   * Returns base of rectangle
   * @return radius
   ************************************************************/
   public double getBase(){
      return myBase;
   }
   
   /**************************************************************
   * Returns the rectangle's height
   * @return height
   ***************************************************************/
   public double getHeight(){
      return myHeight;
   }
   /**
   * Set base of the rectangle
   * @param x sets myBase equal to x
   */
   public void setBase(double x){
      myBase = x;
   }
   /**
   * Set the height of the rectangle
   * @param x sets myHeight equal to x
   */
   public void setHeight(double x){
      myHeight = x;
   }
   /**
   * Implements findArea method in Shape. Finds the area of the rectangle
   * @return Rectangle's area
   */
   public double findArea(){
   
      return myBase * myHeight;
   }
   /**
   * Find the perimeter of rectangle.
   * @return perimeter
   */
   public double findPerimeter(){
   
      return (2*myBase)+(2*myHeight);
   }
   
   /**
   * Find length of diagonal using the Pythagorean Theorem
   * @return diagonal length
   */
   public double findDiagonal(){
      double baseSquared = Math.pow(myBase,2);
      double heightSquared = Math.pow(myHeight,2);
      
      return Math.sqrt(baseSquared + heightSquared);
   }
   
   
}