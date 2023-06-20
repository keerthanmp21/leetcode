#two pointers
#tc O(n), sc O(1)
class Solution:
    def trap(self, height):
        if not height:
            return 0
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l<r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax-height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax-height[r]
        return res

#monotonic stack
# tc O(n), sc O(n)
class Solution2:
    def trap(self, height):
        stack = []
        traps = 0
        #monotonic decreasing stack
        for i, h in enumerate(height):
            while stack and h>height[stack[-1]]:
                bottom = stack.pop()
                if stack:
                    minHeight = min(h, height[stack[-1]])
                    trapHeight = minHeight-height[bottom]
                    width = i-stack[-1]-1
                    traps += trapHeight*width

            stack.append(i)
        return traps

#brute force
#tc O(n^2), sc O(1)
class Solution3:
    def trap(self, height):
        N = len(height)
        traps = 0

        for i in range(N):
            leftMax = 0
            for j in range(i):
                leftMax = max(leftMax, height[j])

            rightMax = 0
            for j in range(i+1,N):
                rightMax = max(rightMax, height[j])
            
            curTrap = min(leftMax, rightMax)-height[i]
            traps += curTrap if curTrap>0 else 0

        return traps
        
# dp iterative
# tc O(n), sc O(n)
class Solution4:
    def trap(self, height):
        N = len(height)
        if N<=2:
            return 0
        leftMax, rightMax = [0]*N, [0]*N
        leftMax[0], rightMax[N-1] = height[0], height[N-1]

        for i in range(1,N):
            leftMax[i] = max(leftMax[i-1],height[i])

        for i in range(N-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])

        traps = 0
        for i in range(N):
            traps += min(leftMax[i], rightMax[i]) -height[i]

        return traps
