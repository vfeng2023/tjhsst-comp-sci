  //Name______________________________ Date_____________
  
   import java.io.*;       		 //the File class
   import java.util.*;     		 //the Scanner class
   import javax.swing.JOptionPane;
    public class Driver10
   {
       public static void main(String[] args) throws Exception
      {
         Song[] songList = input();
         int totalTime = calcTime(songList);
         int longestSong = searchLongestSong(songList);
         display(songList, totalTime, longestSong);
         System.exit(0);
      }
   	
       public static Song[] input() throws Exception 
      {
          String filename = JOptionPane.showInputDialog("Enter file name.");
          Scanner sc = new Scanner(new File(filename));
          int size = Integer.parseInt(sc.nextLine());
          Song[] songs = new Song[size];
          for(int i=0;i<songs.length;i++){
//             String val = sc.nextLine();
//             System.out.println(val);
            songs[i] = new Song(sc.nextLine());
          }
          sc.close();
          return songs;
      }
      /**
      * Returns time in seconds
      */
   
       public static int calcTime(Song[] songs)
      {
         int totalMin = 0;
         int totalSec = 0;
         for(int k=0;k<songs.length;k++){
            totalMin += songs[k].getMinutes();
            totalSec += songs[k].getSeconds();
         }
         return totalMin*60+totalSec;
      }
      
       public static int searchLongestSong(Comparable[] songs)
      {     
           int maxIndex = 0;
           for(int j=0;j<songs.length;j++){
               if(songs[j].compareTo(songs[maxIndex]) > 0){
                  maxIndex = j;
               }
           }
           return maxIndex;
      }
      
       public static void display(Song[] array, int total, int longestSong)
      {
          System.out.println("Total time: "+total/60+"'"+total%60+"\"");
          System.out.println("Longest song: "+array[longestSong].toString());
      }
   }