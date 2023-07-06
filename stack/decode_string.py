class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ''
        curDigit = 0
        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(curDigit)
                curString = ''
                curDigit = 0
            elif char == ']':
                digit = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString*digit
            elif char.isdigit():
                curDigit = curDigit*10 + int(char)
            else:
                curString += char
        return curString