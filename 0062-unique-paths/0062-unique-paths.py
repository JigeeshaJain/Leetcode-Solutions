class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dynamic programming
        
        row=[1]*n #this is going to be the bottom row 
        
        for i in range(m-1): #m-1 is taken as last row is all ones 
            newRow=[1]*n #initially it will have all 1s as its value 
            for j in range(n-2,-1,-1):
                newRow[j]= newRow[ j + 1] + row[ j ]
            row=newRow
        return row[0]
        
        