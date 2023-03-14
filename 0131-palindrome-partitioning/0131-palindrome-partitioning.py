class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[] #collection/ lists of various partions 
        part=[] #this is current partition 
        
        def dfs(i): 
            if i>=len(s): #when there r no more characters to add i.e. aab is already taken into consideration i.e. we have found our match
                res.append(part.copy()) #we need to make a copy as there is a single variable part and we have a recursive loop
                return 
            for j in range(i, len(s)):
                if self.isPalin(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    def isPalin(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True
            
                
        
            
        
        