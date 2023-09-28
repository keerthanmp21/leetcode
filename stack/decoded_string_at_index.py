class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = [0] # total alpha till that point

        for i in range(len(s)):
            if s[i].isdigit():
                length = stack[-1] * int(s[i])
            else:
                length = stack[-1] + 1
            stack.append(length)

        N = len(stack)
        while stack:
            k = k % stack[-1]
            N -= 1
            if k == 0 and s[N-1].isalpha():
                return s[N-1]
            stack.pop()

        return ''
    
s = Solution()
print(s.decodeAtIndex('leet2code3',7))