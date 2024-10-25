from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque()
        q.append(("0000", 0))
        visit = set(deadends)

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
            return res

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    q.append((child, turns + 1))
                    visit.add(child)

        return -1

'''
The time and space complexity of the `openLock` function can be analyzed as follows:

### Time Complexity:
1. **Breadth-First Search (BFS)**: The function uses a BFS approach to explore all
 possible combinations of the lock. Each lock state can be represented as a 4-digit 
 string, resulting in \(10^4 = 10,000\) possible states (from "0000" to "9999").
2. **Children Generation**: For each lock state, the function generates up to 8 
children (2 for each of the 4 positions).
3. **Overall Complexity**: In the worst case, we may need to visit all \(10,000\) 
states, and for each state, we generate 8 children. Thus, the time complexity is:
   O(10^4⋅8)=O(10^4)

### Space Complexity:
1. **Queue**: The BFS queue can store all possible states. In the worst case, it could store up to \(10,000\) states.
2. **Visited Set**: The `visited` set also needs to store all possible states, leading to another \(O(10^4)\) space usage.
3. **Overall Complexity**: Therefore, the space complexity is:
   [O(10^4)]

### Summary:
- **Time Complexity**: \(O(10^4)\)
- **Space Complexity**: \(O(10^4)\)
'''