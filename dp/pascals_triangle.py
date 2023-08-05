from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for _ in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for i in range(len(res[-1])+1):
                row.append(temp[i]+temp[i+1])
            res.append(row)
        return res
    
s = Solution()
print(s.generate(5))