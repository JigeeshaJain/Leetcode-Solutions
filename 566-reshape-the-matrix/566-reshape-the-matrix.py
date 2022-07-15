class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0]) #declaring the rows and columns   
        if m*n!=r*c: return mat
        output=[]
        
        for i in range(r):
            output.append([0]*c)
            
        
        sr=0 #counters for starting row and columns
        sc=0 
        
        for i in range(m):
            for j in range(n):
                if sc==c: #if the matrix has reached the column number then sc i.e. clmn pointer will be reset to 0 and row cntr will be increased so that the value is stored in the next row 
                    sc=0
                    sr+=1
                output[sr][sc]=mat[i][j]
                sc+=1
        return output
        
        
        
                
                