class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res=[]
        
        def backtracking(open1, close):
            if open1==close==n:
                res.append("".join(stack))
                return
            if open1< n:
                stack.append("(")
                backtracking(open1+1,close)
                stack.pop()
            if close<open1:
                stack.append(")")
                backtracking(open1,close+1)
                stack.pop()
            
        backtracking(0,0)
        return res
        
                
                
        
        