package matrix;

public class search_2d_matrix {
    
}

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length, COLS = matrix[0].length;
        int top = 0, bot = ROWS - 1;
        int row = -1;

        while(top <= bot){
            row = (top + bot)/2;
            if(target > matrix[row][COLS - 1]){
                top = row + 1;
            }
            else if(target < matrix[row][0]){
                bot = row - 1;
            }
            else{
                break;
            }
        }

        if(!(top <= bot)){
            return false;
        }

        int l = 0, r = COLS - 1;
        while(l <= r){
            int mid = (l + r)/2;
            if(target < matrix[row][mid]){
                r = mid - 1;
            }
            else if(target > matrix[row][mid]){
                l = mid + 1;
            }
            else{
                return true;
            }
        }

        return false;

    }
}