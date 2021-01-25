public class Distance implements Comparable<Distance>
{
   private int myFeet,myInches;
   public Distance(){
   
      myFeet = myInches = 0;
   }
   public Distance(int x){
      
      myFeet = x;
      myInches = 0;
   
   }
   public Distance(int x,int y){
      
      myFeet = x;
      myInches = y;
   }
   public int getFeet(){
      
      return myFeet;
   }
   public int getInches(){
      
      return myInches;
   }
   public void setFeet(int x){
      
      myFeet = x;
   }
   public void setInches(int x){
   
      myInches = x;
   }
   public int compareTo(Distance d){
      
      if(myFeet < d.getFeet()) return -1;
      if (myFeet > d.getFeet()) return 1;
      if (myInches < d.getInches()) return -1;
      if (myInches > d.getInches()) return 1;
      
      return 0;
   }
   public boolean equals(Distance arg){
      
      return compareTo(arg) == 0;
   }
   public String toString(){
      
      return myFeet +" ft. " + myInches + " in.";
   }

}