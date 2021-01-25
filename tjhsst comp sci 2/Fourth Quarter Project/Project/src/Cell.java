/**
* The Cell class represents a single square on the Game of Life. A cell knows how to draw itself, and its state.
* @author Vivian Feng and Shriya Muthukumar, authored by Vivian Feng
* @version stub
*/
import java.awt.*;//Graphics classes
public class Cell{
   /**
   * whether the cell is alive or dead - alive=true,dead=false
   */
   private boolean state;
   /**
   * x-coordinate of cell on canvas
   */   
   private double x;
   /**
   * y-coordinate of cell on canvas
   */
   private double y;
   /**
   * length of one side of cell
   */
   private double size; 
   
   /**
   * Cell class constructor
   * @param initState inital state of cell
   * @param x x coordinate of cell's upper left corner
   * @param y y coordinate of cell's upper left corner
   * @param side length of the side of the cell square
   */
   public Cell(boolean initState,double x,double y,double side){
      state = initState;
      this.x = x;
      this.y = y;
      this.size = side;
   }
   /**
   * Get state of cell. If cell is alive, getState returns true. Otherwise, get state returns false.
   * @return state of cell
   */
   public boolean getState(){
      return state;
   }
   /**
   * Changes state of cell. If s is true, the state of the is alive. If s is false, the cell is dead.
   * @param s state of cell
   */
   public void setState(boolean s){
      state = s;
   }
   
   /**
   * Draws cell onto a Graphics object. Blue - dead cell. white - living cell
   * @param buffer which graphics object cell will be drawn on.
   */
   public void drawCell(Graphics buffer){
      Color cellColor;
      if(state == true){
        cellColor = new Color(255,254,253);
      }
      else{
         cellColor = new Color(50, 43,145);
      }
      
      buffer.setColor(cellColor);
      buffer.fillRect((int)x,(int)y,(int)size,(int)size);
      buffer.setColor(Color.BLACK);
      buffer.drawRect((int)x,(int)y,(int)size,(int)size);
   
   } 
}