class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitToChar={"2":"abc", "3":"def","4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        
        def backtrack(i, curStr):
            if len(curStr)==len(digits): #base case 
                res.append(curStr)
                return 
            
            for c in digitToChar[digits[i]]:  #digits[i] will give the current digit we are at. so 9 is asociated wid wxyz so we need to map those digits to the characters assosiacted with it. and then we have to brute force it through every character in that string and use backtracking.
                
                backtrack(i+1,curStr+c)
                
        if digits: #coz if it is empty we would return [""] as the output which is our first case/ base case 
            
            backtrack(0,"")
        return res
                
        
        
        
        
        