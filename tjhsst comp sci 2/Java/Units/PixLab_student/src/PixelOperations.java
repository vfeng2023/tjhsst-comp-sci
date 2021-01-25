   //
   // Torbert, 24 July 2013
	//
   import java.awt.Color;
   import java.awt.image.BufferedImage;
	//
   public class PixelOperations
   {
      public Color[][] getArray(BufferedImage img)
      {
         Color[][] arr;
      	//
         int numcols = img.getWidth();
         int numrows = img.getHeight();
      	//
         arr = new Color[numrows][numcols];
      	//
         for(int j = 0; j < arr.length; j++)
         {
            for(int k = 0; k < arr[0].length; k++)
            {
               int rgb = img.getRGB(k,j);
            	//
               arr[j][k] = new Color(rgb);
            }
         }
      	//
         return arr;
      }
      public void setImage(BufferedImage img, Color[][] arr)
      {
         for(int j = 0; j < arr.length; j++)
         {
            for(int k = 0; k < arr[0].length; k++)
            {
               Color tmp = arr[j][k];
               //
               int rgb = tmp.getRGB();
               //
               img.setRGB(k,j,rgb);
            }
         }
      }
      //
   	/**********************************************************************/
   	//
   	// pixel operations
   	// 
      public void zeroBlue(Color[][] arr)
      {
         for(int j = 0; j < arr.length; j++)
         {
            for(int k = 0; k < arr[0].length; k++)
            {
               Color tmp = arr[j][k];
               arr[j][k] = new Color( tmp.getRed(), tmp.getGreen(), 0 );
            }
         }
      }
   	//--------> your new methods go here   <--------------
      //negate all pixels in a picture by setting each color’s value to 255 minus the current value.
   	public void negate(Color[][] arr){
      
         for (int x = 0;x<arr.length;x++){
            
            for(int y = 0;y<arr[0].length;y++){
               Color tmp = arr[x][y];
               arr[x][y] = new Color(255-tmp.getRed(),255-tmp.getGreen(),255-tmp.getBlue());
            }
         }
      }
   /*
    grayscale turns picture into shades of gray by setting the red, green, and blue values of each pixel
   to the average of the current red, green, and blue value of the pixel.
   Possible weights: 30% red + 59% green + 11% blue
    */
   public void grayscale(Color[][] pixArray){
      for(int row=0;row<pixArray.length;row++){
         for(int column=0;column<pixArray[0].length;column++){
            Color temp = pixArray[row][column];
            int red = (int)(temp.getRed()*0.3);
            int green = (int)(temp.getGreen()*0.59);
            int blue = (int)(temp.getBlue()*0.11);
            pixArray[row][column] = new Color(red,blue,green);
         }
      }
   }
   /*
      Sepia-toned pictures have a yellowish tint that we associate with older pictures.
      	Set a pixel’s red value to the sum of .393 of its red value, .769 of its green value,
      and .189 of its blue value
      	Set a pixel’s green value to the sum of .349 of its red value, .686 of its green value,
      and .168 of its blue value
      	Set a pixel’s blue value to the sum of .272 of its red value, .534 of its green value,
      and .131 of its blue value

    */
   public void sepiaTone(Color[][] pixArray){
      int oldR, oldG, oldB, newR,newG,newB;
      for(int row=0;row<pixArray.length;row++){
         for(int col=0;col<pixArray[0].length;col++){
            Color tmp = pixArray[row][col];
            oldR = tmp.getRed();
            oldG = tmp.getGreen();
            oldB = tmp.getBlue();
            newR = (int)(oldR*0.393+oldG*0.769+oldB*0.189);
            newG = (int)(oldR*0.349+oldG*0.686+oldB*0.168);
            newB = (int)(oldR*0.272+oldG*0.534+oldB*0.131);

            if(newR > 255) newR=255;
            if(newG > 255) newG = 255;
            if(newB > 255) newB = 255;

            pixArray[row][col] = new Color(newR,newG,newB);
         }
      }
   }
   /*
      blur - set the current pixel’s color to the average of the colors of the current pixel and its
      four neighboring pixels.
    */
   public void blur(Color[][] pixArray,Color[][] copy){
      int red,blue,green;
      for(int row=0;row<pixArray.length;row++){
         for(int col=0;col<pixArray[0].length;col++){
            if(row-1>=0&&col-1>=0&&row+1<pixArray.length&&col+1<pixArray[0].length){
               Color tmp = copy[row][col];
               Color top = copy[row-1][col];
               Color bottom = copy[row+1][col];
               Color left = copy[row][col-1];
               Color right = copy[row][col+1];
               red = (top.getRed()+bottom.getRed()+left.getRed()+tmp.getRed()+right.getRed())/5;
               green = (top.getGreen()+bottom.getGreen()+left.getGreen()+tmp.getGreen()+right.getGreen())/5;
               blue = (top.getBlue()+bottom.getBlue()+left.getBlue()+tmp.getBlue()+right.getBlue())/5;
               pixArray[row][col] = new Color(red,green,blue);
            }
         }
      }
   }
   /*
      posterize - A bunch of different colors gets set to just a few colors.  For a range of colors, map them to a single color.
    */
   public void posterize(Color[][] pixArray){
      int oldRed,oldGreen,oldBlue;
      int[] color;
      for(int row=0;row<pixArray.length;row++){
         for(int col=0;col<pixArray[0].length;col++){
            Color tmp = pixArray[row][col];
            color = new int[]{tmp.getRed(), tmp.getGreen(), tmp.getBlue()};
            for(int index=0;index<color.length;index++){
               if(0<=color[index]&&color[index]<63){
                  color[index] = 32;
               }
               else if(63<=color[index]&&color[index]<126){
                  color[index] = 94;
               }
               else if(126<=color[index]&&color[index]<189){
                  color[index] = 158;
               }
               else{
                  color[index] = 221;
               }
            }
            pixArray[row][col] = new Color(color[0],color[1],color[2]);
         }
      }
   }
   /*
      Color Splash - Turn a picture into a grayscale, except for the red colors, which are made a solid red.
    */
   public void colorSplash(Color[][] pixArray){
      for(int row=0;row<pixArray.length;row++){
         for(int column=0;column<pixArray[0].length;column++){
            Color temp = pixArray[row][column];
            if (temp.getRed() > 200 && temp.getBlue() < 75 && temp.getGreen() <75) {
               pixArray[row][column] = new Color(255,0,0);

            }else{
               int red = (int) (temp.getRed() * 0.3);
               int green = (int) (temp.getGreen() * 0.59);
               int blue = (int) (temp.getBlue() * 0.11);
               pixArray[row][column] = new Color(red, blue, green);
            }
         }
      }
   }
   /*mirrorLR: Mirrors the left side of the picture onto the right side of the picture.  Get a pixel from the left side of
   the picture and copy it onto a pixel on the right side of the picture that is on the same row and the same distance from
    the right end that the left pixel is from the left end. */
  public void mirrorLR(Color[][] arr){

      for (int x=0;x<arr.length;x++){

         for(int y=0;y<arr[0].length;y++){
            Color tmp = arr[x][(arr[0].length-1)-y];
            arr[x][y] = new Color(tmp.getRed(),tmp.getGreen(),tmp.getBlue());
         }

      }
  }
      public void mirrorUD(Color[][] arr){

         for (int x=0;x<arr.length;x++){

            for(int y=0;y<arr[0].length;y++){
               Color tmp = arr[(arr.length-1)-x][y];
               arr[x][y] = new Color(tmp.getRed(),tmp.getGreen(),tmp.getBlue());
            }

         }
      }
   	
     
   }
   //
	// end of file
	//