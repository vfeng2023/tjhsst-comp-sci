	 //Torbert, e-mail: smtorbert@fcps.edu
	 //version 7.22.2003
    //mlbillington@fcps.edu  7.17.2018  uses PrintWriter
   import java.io.*;
    public class MakeDataFile
   {
       public static void main(String[] args) throws Exception
      {
         PrintWriter pw = new PrintWriter(new FileWriter("data.txt"));
         int numitems = 28;
         pw.println(numitems);
         for(int k = 0; k < numitems; k++)
         {
            pw.println((int)(Math.random()*100));
            pw.println((int)(Math.random() * 12));
         }
         pw.close();
      }
   }