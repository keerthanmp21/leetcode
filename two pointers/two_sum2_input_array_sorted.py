from typing import List

# binary search
# tc O(n), sc O(1)
class Solution:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            curSum = numbers[l]+numbers[r]
            if curSum<target:
                l+=1
            elif curSum>target:
                r-=1
            else:
                return [l+1, r+1]
        return []
    
    def twoSum(self, numbers, target):
        N = len(numbers)
        for i in range(N):
            l, r = i+1, N-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1