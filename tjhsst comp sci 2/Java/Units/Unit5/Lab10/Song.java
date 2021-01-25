//Name______________________________ Date_____________

    public class Song implements Comparable<Song>
   {
   	//data fields
      private String myTitle;
      private int myMinutes, mySeconds;
   
   	//constructors
       public Song(String toBeParsed)
      {
         //find colon
         int colonAt = toBeParsed.indexOf(':');
         //parse min
         myMinutes = Integer.parseInt(toBeParsed.substring(0,colonAt));
         //parse sec
         mySeconds = Integer.parseInt(toBeParsed.substring(colonAt+1,colonAt+3));
         //parse title	
         myTitle = toBeParsed.substring(colonAt+4);
      }
     
   	//accessors and modifiers
      public int getMinutes() {
         return myMinutes;
      }
      public int getSeconds(){
         return mySeconds;
      }
      public String getTitle(){
         return myTitle;
   	}
       
      //other methods:  compareTo(), equals(), toString()
      public int compareTo(Song s){
         return(myMinutes*60+mySeconds - (s.getMinutes()*60+s.getSeconds()));
      }
   	public boolean equals(Song s){
         return compareTo(s) == 0;
      }
      
      public String toString(){
         return myTitle + "("+myMinutes+"'"+mySeconds+"\")";
      }
   	
   }