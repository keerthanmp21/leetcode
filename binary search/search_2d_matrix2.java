public class search_2d_matrix2 {
    
}
// tc O(m*logn)
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length, COLS = matrix[0].length;
        for(int row = 0; row < ROWS; row++){
            int l = 0, r = matrix[row].length-1;
            while(l <= r){
                int mid = (l + r) / 2;
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
        }
        return false;
    }
}