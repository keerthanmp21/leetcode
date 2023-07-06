# tc O(n), sc O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True