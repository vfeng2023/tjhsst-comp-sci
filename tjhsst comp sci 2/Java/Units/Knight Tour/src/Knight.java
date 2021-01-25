import java.util.Arrays;

public class Knight {
    static final int N = 8;

    public static boolean isValid(int i, int j, int sol[][]) {
        if (i>=0 && i<N && j>=0 && j<N) {
            if(sol[i][j]==-1)
                return true;
        }
        return false;
    }

//    public static boolean isValid(int col, int row,int[][] grid)  {
//        if ((0 <= row && row < N) && (0 <= col && col < N) && (grid[row][col] == -1)) {
//            return true;
//        }
//        return false;
//    }
//    public static boolean knightTour(int sol[][], int i, int j, int stepCount, int xMove[], int yMove[]) {
//        if (stepCount == N*N)
//            return true;
//
//        for(int k=0; k<8; k++) {
//            int nextI = i+xMove[k];
//            int nextJ = j+yMove[k];
//
//            if(isValid(nextI, nextJ, sol)) {
//                sol[nextI][nextJ] = stepCount;
//                if (knightTour(sol, nextI, nextJ, stepCount+1, xMove, yMove))
//                    return true;
//                sol[nextI][nextJ] = -1; // backtracking
//            }
//        }
//
//        return false;
//    }
public static boolean knightTour(int[][] grid, int row, int col, int count,int[] xstep,int[] ystep) {
    if (count == N * N+1) {
        return true;
    }

    //for each move see if next square is valid:
    for (int i = 0; i < xstep.length; i++) {
        int poss_r = row + xstep[i];
        int poss_c = col + ystep[i];
        //if a move is valid look ahead to the other paths:
        if (isValid(poss_c,poss_r,grid)) {
            //call move again
            grid[poss_c][poss_r] = count;
            //if future paths are valid make grid[new r, new c] = count+1
            if (knightTour(grid, poss_r, poss_c, count + 1,xstep,ystep)) {
//                row = poss_r;
//                col = poss_c;
//                count+=1;
                return true;
            }
            grid[poss_c][poss_r] = -1;
            //return true
        }
        //if non are valid return false

    }
    return false;
}
//    public static boolean startKnightTour() {
//        int[][] sol = new int[N][N];
//
//        for(int i=0; i<N; i++) {
//            for(int j=0; j<N; j++) {
//                sol[i][j] = -1;
//            }
//        }
//
//        int xMove[] = {2, 1, -1, -2, -2, -1, 1, 2};
//        int yMove[] = {1, 2, 2, 1, -1, -2, -2, -1};
//
//        sol[0][0] = 0; // placing knight at cell(1, 1)
//
//        if (knightTour(sol, 0, 0, 1, xMove, yMove)) {
//            for(int i=0; i<N; i++) {
//                System.out.println(Arrays.toString(sol[i]));
//            }
//        }
//        return false;
//    }
    public static void startKnightTour(){
        int count = 1;
        int[][] grid = new int[N][N];

        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                grid[i][j] = -1;
            }
        }
        int xstep[] = {2, 1, -1, -2, -2, -1, 1, 2};
        int ystep[] = {1, 2, 2, 1, -1, -2, -2, -1};
        grid[0][0] = count;
        if(knightTour(grid,0,0,count+1,xstep,ystep)){
            for(int i=0;i<N;i++){
                System.out.println(Arrays.toString(grid[i]));
            }
        }

    }

    public static void main(String[] args) {
        startKnightTour();
    }
}
