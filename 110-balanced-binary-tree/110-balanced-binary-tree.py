# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True,0]
        
            left, right = dfs(root.left), dfs(root.right)  #using recursive function to check whether left and right subtrees are balanced or not 
            balanced =left[0] and right[0] and abs(left[1]-right[1])<=1 
            #here left[0] means left subtree is balanced as left[0] shouldbe True and for it to be true it should be balanced. So, the statement means that left, right, are we balanced from the root subtree if everything is True then it will proceed
            return [balanced, 1+ max(left[1], right[1])]
        
        return dfs(root)[0] #here we have taken [0] i.e. index 0 coz 
    
            