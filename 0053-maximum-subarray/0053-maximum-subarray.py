class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        currSum=0
        
        for i in nums:
            if currSum<0:
                currSum=0  #reseting the sum to 0 if the sum goes negative
            currSum+=i
            maxSub=max(currSum,maxSub)
        return maxSub
            
        
        