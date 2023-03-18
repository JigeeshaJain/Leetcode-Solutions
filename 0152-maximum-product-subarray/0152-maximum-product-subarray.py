class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res =max(nums)
        curMin, curMax=1,1
        
        for n in nums:
            if n==0:
                curMin, curMax=1,1
                continue
            tmp=curMax
            curMax=max(curMax*n, curMin*n, n)
            curMin=min(tmp*n, curMin*n, n)
            res=max(curMax, res)
        return res 
            
        
    
        
        