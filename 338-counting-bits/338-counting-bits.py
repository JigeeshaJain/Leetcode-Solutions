class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        offset=1
        
        for i in range(1, n+1):
            
            if offset*2==i: # here we multiply and compare wid i as we r checking the most significant bit i.e. 1,2,4,8 and if i is that then we update the value of offset acc.
                offset=i
            dp[i]=1+dp[i-offset] #here the number of 1s are same 
            
        return dp
        
            
        