	//Name______________________________ Date_____________
   public class EMail
   {
      private String myUserName;
      private String myHostName;
      private String myExtension;
      public EMail(String address)
      {
         //get index of @ and .
         int part1Ind = address.indexOf('@');
         int part2Ind = address.indexOf('.');
         //split accordingly
         myUserName = address.substring(0,part1Ind);
         myHostName = address.substring(part1Ind+1,part2Ind);
         myExtension = address.substring(part2Ind+1);
      }
      public String getUserName()
      {
         return myUserName;
      }
      public String getHostName()
      {
         return myHostName;
      }
      public String getExtension()
      {
         return myExtension;
      }
      public String toString()
      {
         return myUserName+"@"+myHostName+"."+myExtension;
      }
   }