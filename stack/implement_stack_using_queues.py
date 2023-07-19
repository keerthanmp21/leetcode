from collections import deque as Deque

class MyStack:

    def __init__(self):
        self.q = Deque()

    def push(self, x: int) -> None:
        temp = Deque([x])
        # if we dont want to create new deque then we can use rotate logic
        '''
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        '''
        temp.extend(self.q)
        self.q = temp

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()