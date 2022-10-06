class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        sum1=int(n/2*(n-1)) #here 2*a is 0 as a is always 0 and d is 1 as sum=n/2(2a+(n-1)d
        res=sum1-sum(nums)
        return res
    
        