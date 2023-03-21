class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i>=len(candidates) or total>target:
                return
                
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i]) #here total will change as we append i to the list of curr
            curr.pop()
            dfs(i+1, curr, total) #here total will remain as it is as we are not adding the element to it 
            
        dfs(0,[],0)
        return res
            
            
            
            
        
        
        