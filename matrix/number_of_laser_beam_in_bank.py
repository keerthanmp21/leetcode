from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ROWS, COLS = len(bank), len(bank[0])
        laser_cell = {}
        
        for r in range(ROWS):
            laser_cell[r] = 0
            for c in range(COLS):
                if bank[r][c] == '1':
                    laser_cell[r] += 1
        
        total_beams = 0

        for r in range(ROWS - 1):
            for nextRow in range(r + 1, ROWS):
                if laser_cell[r] > 0 and laser_cell[nextRow] > 0:
                    total_beams += laser_cell[r] * laser_cell[nextRow]
                    break

        return total_beams
            