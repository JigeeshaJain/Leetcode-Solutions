class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2=0,0 #initializing the rob pointers to the starting two values 
        for n in nums:
            temp= max(rob1+n, rob2)
            rob1=rob2
            rob2=temp
        return rob2
            
        