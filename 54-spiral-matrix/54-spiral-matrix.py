class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right=0, len(matrix[0]) #length of columns 
        
        top, bottom=0, len(matrix)  # length of rows 
        res=[]
        
        while left< right and top < bottom:
            for i in range(left, right): #if right is 4 then it will go from 0 to 3 i.e out of bounce 4 is non inclusive 
                res.append(matrix[top][i])
            top+=1
            
            for i in range(top, bottom):
                res.append(matrix[i][right-1]) #as right is out of bounce 
            right-=1
            
            if not (left< right and top<bottom):
                break
                           
                           
            for i in range(right-1, left-1, -1): #non inclusive 
                res.append(matrix[bottom-1][i])  #when right to left or left to right column is always going to be i
            bottom-=1
            
            for i in range(bottom-1, top-1, -1): #-1 is added as we r gng in the reverse order 
                res.append(matrix[i][left])
            left+=1
            
                           
        return res