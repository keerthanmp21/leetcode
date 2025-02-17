package matrix;

import java.util.HashMap;
import java.util.Map;

public class number_of_laser_beam_in_bank {
    
}

class Solution {
    public int numberOfBeams(String[] bank) {
        int ROWS = bank.length, COLS = bank[0].length();
        Map<Integer, Integer> laserBeams = new HashMap<>();

        for(int r = 0; r < ROWS; r++){
            laserBeams.put(r, 0);
            for(int c = 0; c < COLS; c++){
                if(bank[r].charAt(c) == '1'){
                    int val = laserBeams.get(r) + 1;
                    laserBeams.put(r, val);
                }
            }
        }

        int totalBeams = 0;
        for(int row = 0; row < ROWS; row++){
            for(int nextRow = row + 1; nextRow < ROWS; nextRow++){
                if(laserBeams.get(row) > 0 && laserBeams.get(nextRow) > 0){
                    totalBeams += laserBeams.get(row) * laserBeams.get(nextRow);
                    break;
                }
            }
        }

        return totalBeams;

    }
}