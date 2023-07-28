from typing import List

class Solution:
    #  tc O(n*n!), sc O(n!)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        count={n:0 for n in nums}
        for n in nums:
            count[n]+=1
        N = len(nums)
        def dfs():
            if len(perm)== N:
                res.append(perm.copy())
                return
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    perm.pop()
        dfs()
        return res