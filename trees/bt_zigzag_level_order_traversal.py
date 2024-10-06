from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        isRightToLeft = True

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if isRightToLeft:
                res.append(temp)
                isRightToLeft = False
            else:
                res.append(temp[::-1])
                isRightToLeft = True
            
        return res
    
'''
The `zigzagLevelOrder` function implements a zigzag (or spiral) level-order traversal 
of a binary tree. Let's analyze its time and space complexities.

### Function Explanation
The function uses a deque to efficiently handle the queue operations and toggles the 
order of node values added to the result list based on the `isRightToLeft` flag. If 
the flag is `True`, it appends the level as is; if `False`, it appends the reversed 
level.

### Time Complexity
The time complexity is \(O(N)\), where \(N\) is the number of nodes in the binary tree.
 Each node is visited once, and their values are processed in constant time.

### Space Complexity
The space complexity is \(O(W)\), where \(W\) is the maximum width of the tree. This 
is because, in the worst case (for a complete binary tree), the queue can store all 
the nodes at the deepest level, which could be approximately \(N/2\).

### Summary
- **Time Complexity:** \(O(N)\)
- **Space Complexity:** \(O(W)\) (up to \(O(N)\) in the worst case)

### Additional Considerations
- The use of `deque` for queue operations allows \(O(1)\) time complexity for both 
appending and popping elements, making it efficient for level-order traversal.
- The toggle between right-to-left and left-to-right traversal is handled efficiently 
with a simple boolean flag. 

Overall, the implementation is efficient and correctly performs zigzag traversal of 
the binary tree.
'''