class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        min_val = min(val, self.getMin())
        '''
        stack has val and min_val
        val is the value which need to be pushed into thestack
        min_val is the value which is minimum till that point
        irrespective of push value
        '''
        self.stack.append((val, min_val))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()