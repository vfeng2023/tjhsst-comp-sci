	//Name:Vivian Feng    Date: Jun 17,2020 
  
   import java.io.*;             //the File class
   import java.util.*;   		   //the Scanner class
   import javax.swing.*;         //the JOptionPane class
   import java.util.Arrays;
    public class Driver09
   {
       public static void main(String[] args) throws Exception
      {
         String[] array = input("data.txt");
         for(int k = 0; k < array.length; k++)
            array[k] = convert(array[k]);
         Arrays.sort(array);              //why don't you have to implement sort()?
         output(array, "output.txt");
      }
   	
       public static String[] input(String filename)
      {
         Scanner infile = null;
         try{
            infile = new Scanner(new File(filename));
         }
             catch(FileNotFoundException e)
            {
               JOptionPane.showMessageDialog(null,"The file could not be found.");
               System.exit(0);
            }
         int numitems = infile.nextInt();
         String[] array = new String[numitems];
         for(int k = 0; k < numitems; k++)
         {
            array[k] = infile.next();
         }
         infile.close();
         return array;
      }
   	
       public static String convert(String website)
      {
         String packageName="";
         int pos=website.length()-1;
         String part="";
         while(pos >= website.indexOf('.')){
            if(website.charAt(pos)=='.') {
               packageName += new StringBuilder(part).reverse().toString();
               if(pos!=website.indexOf('.')) packageName += ".";
               part = "";   
               }
            else part += website.charAt(pos);
            pos --;
         }      
         
         return packageName;
      }
   	
       public static void output(String[] array, String filename) throws Exception
      {  
         System.out.println(Arrays.toString(array));
         PrintWriter outfile = new PrintWriter(new FileWriter(filename));
         for(int k = 0; k < array.length; k++)
            outfile.println(array[k].toString());
          outfile.close();
      }
     
   
   }