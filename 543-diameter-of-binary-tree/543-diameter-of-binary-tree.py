# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res =[0]
        def dfs(root):
            if not root:
                return -1
            left=dfs(root.left) #left will store the height of left subtree
            right=dfs(root.right)
            res[0]=max(res[0],2+left+right) # will give the diameter 
            
            return 1+max(left,right)  #return the height 
    
    
        dfs(root)
        return res[0]
            
        
        