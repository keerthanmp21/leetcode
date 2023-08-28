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
