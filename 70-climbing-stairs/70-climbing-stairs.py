class Solution:
    def climbStairs(self, n: int) -> int:
        one, two=1,1  #two pointers are taken as one for 1 step and two for step 2 also it uses dynamic programming 
        for i in range (n-1):
                temp=one
                one=one+two
                two=temp
        return one
            
        
        
        
        
        
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        