import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import java.awt.*;

public class Main {
  public static void main(String[] args) {  
        Picture arch = new Picture("arch.jpg");
       // arch.show();
        // switchColors() is defined in the Picture.java file
        arch.switchColors();
        arch.show();
      }
} 
