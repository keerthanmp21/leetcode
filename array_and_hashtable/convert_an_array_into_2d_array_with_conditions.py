from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        no_of_occurrences = {}
        for i in nums:
            no_of_occurrences[i] = no_of_occurrences.get(i,0) + 1
        
        res = []
        for _ in range(max(no_of_occurrences.values())):
            temp = []
            for key, value in list(no_of_occurrences.items()):
                if value != 0:
                    temp.append(key)
                no_of_occurrences[key] -= 1
                if no_of_occurrences[key] == 0:
                    del no_of_occurrences[key]
            res.append(temp)

        return res

