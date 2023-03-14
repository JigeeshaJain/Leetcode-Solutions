class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols=len(board), len(board[0])
        path=set() #inorder to avoid that we do not revisit the ssame location twice
        
        def dfs(r, c, i): #current character in the target word that we r looking for i.e. if we find theword then 
            if i ==len(word):
                return True
            if (r<0 or c<0 or 
                r>=rows or c>=cols or 
                word[i]!=board[r][c] or 
                (r,c) in path): 
                return False
            
            path.add((r,c))  #here we have taken i+1 cuz we found the character we r looking for and now we have to fidn the next character in the target word 
            res= (dfs(r+1,c,i+1) or
                 dfs(r-1,c,i+1) or
                 dfs(r,c+1,i+1) or
                  dfs(r,c-1,i+1)) 
            path.remove((r,c)) # as we have already visited that location
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True #here 0 is passed as we r starting from beginning of the word 
        return False 
        