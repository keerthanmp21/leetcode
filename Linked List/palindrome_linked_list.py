from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        lenght = 0
        temp = head
        while temp:
            lenght += 1
            temp = temp.next

        temp = head
        if lenght % 2:  # odd
            curCnt = 0
            while curCnt <= lenght // 2:
                curCnt += 1
                stack.append(temp.val)
                temp = temp.next
            stack.pop()
        else:  # even
            curCnt = 0
            temp = head
            while curCnt < lenght // 2:
                curCnt += 1
                stack.append(temp.val)
                temp = temp.next

        while stack:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        return True

'''
To analyze the time and space complexity of the given `isPalindrome` function, let's 
break it down:

### Time Complexity
1. **Calculating total length**: 
   - The first `while` loop traverses the entire linked list once to calculate the 
   total length, which takes (O(n)), where (n) is the number of nodes in the 
   list.

2. **Pushing values onto the stack**: 
   - The second part of the function again traverses the first half of the linked list 
   (up to (n/2)), which also takes (O(n)).

3. **Comparing values**:
   - The final loop compares the elements in the stack with the second half of the 
   linked list. This also takes (O(n)) since it goes through half the list 
   (again (n/2)).

Overall, the dominant factor here is the traversal of the list, leading to a total 
time complexity of: [O(n)]

### Space Complexity
1. **Stack Storage**: 
   - The space used for the stack is proportional to the number of nodes stored in it. 
   In the worst case (for an odd-length palindrome), you are storing (n/2) elements in
    the stack.
   
Thus, the space complexity is: [O(n)]

### Summary
- **Time Complexity**: (O(n))
- **Space Complexity**: (O(n))

If you were to optimize space complexity, you could modify the approach to use two 
pointers to avoid using extra space, achieving (O(1)) space complexity while still 
maintaining (O(n)) time complexity.
'''