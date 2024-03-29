class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top,bot=0,ROWS-1
        
        while top<=bot:
            mrow= (top+bot)//2
            if target > matrix[mrow][-1] : #if target value is greater than the rightmost element i.e. the greatest element then you have to shift top row as values keep increasing downwards 
                top =mrow+1
            elif target < matrix[mrow][0]: #if target value is less than the leftmost mid row value then we need to move up i.e. shift our bottom pointer upwards
                bot=mrow -1
            else:
                break
        if not (top<= bot):
            return False
        mrow=(top+bot)//2
        l,r=0,COLS-1
        while l<=r:
            m=(l+r)//2
            if target> matrix[mrow][m]:
                l=m+1
            elif target < matrix[mrow][m]:
                r=m-1
            else:
                return True
        return False
        
        
        
        
                    
        