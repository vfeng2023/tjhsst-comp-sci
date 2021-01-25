	//Name: Vivian FENg Date:UwU
    public class Salesperson 
   {
   	//data fields
      private String myName;
      private int myCars, myTrucks,myTotal;
   
   	//constructors
   
      public Salesperson(String x, int y,int z){
         myName = x;
         myCars = y;
         myTrucks = z;
         myTotal = myCars + myTrucks;
      }
   
   
   	//accessors and modifiers
   
      public int getCars(){
         return myCars;
      }
      public String getName(){
         return myName;
      }
      public int getTrucks(){
         return myTrucks;
      }
      
      public void setCars(int x){
         myCars = x;
      }
      public void setTrucks(int x){
         myTrucks = x;
      }
      
      public int getTotal(){
         myTotal = myCars + myTrucks;
         return myTotal;
      }
   
   
   	//other methods: toString
   
      public String toString(){
         return myName + "\t"+myCars+ "\t" + myTrucks;
      }
   }