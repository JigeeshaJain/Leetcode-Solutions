class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        subset=[]
        
        def dfs(i):
            
            if i>=len(nums):
                res.append(subset.copy())
                return 
            #decision to include in the tree
            subset.append(nums[i])
            dfs(i+1)
            
            #decision not to include in the subset
            subset.pop()
            dfs(i+1)            
        dfs(0)
        return res
        
        
        # res=[[]]
#         l,r=0,1
#         hashmap =set()
#         visited =[]
#         if nums==[]:
#             return res
#         for i in range(len(nums)):
            
#             if not in visited:
#                 visited.append([nums[i]])
#                 res.append([nums[i]])
#             else:
#                 l
                
#         return res
    
#     def dfs(node):
#         if not root:
#             return [[]]
#         for i in range(len(nums)):
            
#             res.append([nums[i]])
            
#             dfs(node.left)
#             dfs(node.right)
            
            
            
            
            
        