/**
* The GamePanel Class is responsible to changing the state of each cell and updating the cell states accordingly
* It also displays the generation count
* @author Vivian Feng and ..., Vivian Feng as main author
* @version stubs
*/
import javax.swing.*; //JPanel
import java.awt.*; //Color
import java.awt.event.*; //animation
import java.awt.image.*; //buffer
public class GamePanel extends JPanel{

	private static	final	int FRAME =	400;
	//add	background color 
	private BufferedImage aniFrame;
	private Graphics aniBuffer;
	//other fields
    private static int numSquares = 20;
	private boolean[][] previousGen=new boolean[numSquares][numSquares];
	;
	private Cell[][] grid;
	private Timer animationTimer;
	private int	genCount;
	private JButton startButton;
	/**
   * GamePanel Constructor, does intital panel setup
   * @param states gives the intial states of all the cells in the grid
   */
	public GamePanel(int[] states){
      setLayout(new FlowLayout());
      // initalize generation count
		genCount = 0;
		//set	up	frames
      aniFrame = new BufferedImage(FRAME,FRAME,BufferedImage.TYPE_INT_RGB);
      aniBuffer = aniFrame.getGraphics();
		//set	up	Cells
      boolean initState;
      grid = new Cell[numSquares][numSquares];

      for(int row=0;row<grid.length;row++){
         for(int column=0;column<grid[0].length;column++){
            if(states[row*20+column] == 1){
               initState = true;
            }
            else{
               initState = false;
            }
            grid[row][column] = new Cell(initState,FRAME/numSquares*row,FRAME/numSquares*column,FRAME/numSquares);
         }
      }
      //set previousGen
		setPreviousGen();
      //draw cells
      aniBuffer.setColor(Color.RED);
      aniBuffer.fillRect(0,0,FRAME,FRAME);
      for(int row =0;row<grid.length;row++){
      	for(int col=0;col<grid[0].length;col++){
      		grid[row][col].drawCell(aniBuffer);
		}
	  }
      aniBuffer.setColor(Color.RED);
      aniBuffer.drawString("Generation: "+genCount,(int)(0.75*FRAME),(int)(0.05*FRAME));
		//set	start	button
		startButton = new JButton("Start Generations");
      	startButton.addActionListener(new StartListener());
      	add(startButton);


	}

	/**
	 * Sets field previousGen to states that correspond with the grid
	 */
	private void setPreviousGen(){
		for(int row=0;row<grid.length;row++){
			for(int column=0;column<grid[0].length;column++){
				previousGen[row][column] = grid[row][column].getState();
			}
		}
	}
   /**
   * Overrides painComponent method from JPanel
   */
	public void	paintComponent(Graphics	g){
		//draw each	frame by loading aniBuffer
      g.drawImage(aniFrame,0,0,getWidth(),getHeight(),null);
		
	}
	/**
   * Listener for Start button
   */
	private class StartListener implements	ActionListener{
		public void	actionPerformed(ActionEvent e){
			//record	intial states in previousGen
			//show intitial generation
         //disable start button
			//start timer
			animationTimer = new Timer(1000,new TimerListener());
			animationTimer.start();
			startButton.setEnabled(false);
			startButton.setVisible(false);
		}
	}
	/**
   * Listener for timer
   */
	private class TimerListener implements	ActionListener{
		public void	actionPerformed(ActionEvent e){
			//clear previous frame
			aniBuffer.fillRect(0,0,FRAME,FRAME);
			//determine	each state of each cell	according to previous generations state stored in previousGen;
			setPreviousGen();
			int[][] moves = new int[][]{{-1,-1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0}};
			//draw and fill each	cell accordingly
			/*
		   Algorithim for determining cell state
		   check all valid booleans
		   if there are 8 neighbors go to general case
			  follow all four rules
			  switch cell state accordingly
		   if there are 5 neigbors go to special case edge edition
			  follow all rules
			  switch cell state accordingly
		   if there are 3 neighbors go to special case corner edition
			  follow all rules except 3
			  switch cell state accordingly
			  */

			for(int row=0;row<grid.length;row++){
				for(int col=0;col<grid[0].length;col++){
					int livingNeighbors = 0;
					//count neighbors(using previousGen) by checking adjacent square
					for(int[] move: moves){
						int x = move[0];
						int y = move[1];
						//count number of living neighbors
						if((0 <= row+x && row+x<grid.length)&&(0<=col+y && col+y<grid.length)){
							if(previousGen[row+x][col+y] == true){
								livingNeighbors++;
							}
						}
					}
					//set cell state using rules for game of life
					if(livingNeighbors < 2) grid[row][col].setState(false);
					else if(livingNeighbors == 3) grid[row][col].setState(true);
					else if(livingNeighbors == 3 || livingNeighbors == 2){ /*Do nothing because cell will stay alive*/}
					else if(livingNeighbors > 3) grid[row][col].setState(false);
					//draw cell
					grid[row][col].drawCell(aniBuffer);

				}
			}
			//increase generation count
			genCount++;
			aniBuffer.setColor(Color.RED);
			aniBuffer.drawString("Generation: "+genCount,(int)(0.75*FRAME),(int)(0.05*FRAME));
			//update	panel	image	to	match
			repaint();
		}
	}
	
	
}