from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        output = 0
        d = {}
        for r in range(len(fruits)):
            if fruits[r] in d:
                d[fruits[r]] += 1
            else:
                if len(d) == 2:
                    output = max(output, sum(d.values()))
                    while len(d) == 2:
                        d[fruits[l]] -= 1
                        if d[fruits[l]] == 0:
                            del d[fruits[l]]
                        l += 1
                d[fruits[r]] = 1
        return max(output, sum(d.values()))
