package matrix;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class valid_sudoku {
    
}

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, HashSet<Character>> rowSet = new HashMap<>();
        Map<Integer, HashSet<Character>> colSet = new HashMap<>();
        Map<String, HashSet<Character>> squareSet = new HashMap<>();

        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                char curChar = board[r][c];
                if(curChar == '.'){
                    continue;
                }
                String squareKey = ((r/3) + "," + (c/3));
                if(rowSet.containsKey(r) && rowSet.get(r).contains(curChar) ||
                colSet.containsKey(c) && colSet.get(c).contains(curChar) ||
                squareSet.containsKey(squareKey) && squareSet.get(squareKey).contains(curChar)){
                    return false;
                }

                rowSet.putIfAbsent(r, new HashSet<>());
                rowSet.get(r).add(curChar);

                colSet.putIfAbsent(c, new HashSet<>());
                colSet.get(c).add(curChar);

                squareSet.putIfAbsent(squareKey, new HashSet<>());
                squareSet.get(squareKey).add(curChar);
            }
        }
        return true;
    }
}